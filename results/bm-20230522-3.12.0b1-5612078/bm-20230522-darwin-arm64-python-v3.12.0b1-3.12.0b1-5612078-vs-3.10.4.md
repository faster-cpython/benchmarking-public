
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b1
- machine: darwin-arm64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 171 ms: 1.18x faster                                       |
| docutils       | 1.78 sec                                               | 1.55 sec: 1.15x faster                                     |
| tornado_http   | 91.9 ms                                                | 71.4 ms: 1.29x faster                                      |
| Geometric mean | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.6 ms: 1.37x faster                                      |
| float          | 72.3 ms                                                | 59.0 ms: 1.23x faster                                      |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.19x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.9 ms: 1.27x faster                                      |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                      |
| regex_dna      | 160 ms                                                 | 150 ms: 1.06x faster                                       |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 188 us: 1.51x faster                                       |
| unpickle_pure_python | 203 us                                                 | 146 us: 1.39x faster                                       |
| json_dumps           | 8.38 ms                                                | 6.53 ms: 1.28x faster                                      |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                     |
| xml_etree_process    | 45.1 ms                                                | 39.3 ms: 1.15x faster                                      |
| unpickle             | 9.77 us                                                | 9.30 us: 1.05x faster                                      |
| pickle               | 7.36 us                                                | 7.49 us: 1.02x slower                                      |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 72.6 ms                                                | 75.8 ms: 1.04x slower                                      |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| xml_etree_generate   | 54.3 ms                                                | 56.7 ms: 1.04x slower                                      |
| pickle_list          | 2.83 us                                                | 2.96 us: 1.05x slower                                      |
| pickle_dict          | 17.8 us                                                | 18.9 us: 1.07x slower                                      |
| unpickle_list        | 2.66 us                                                | 3.21 us: 1.21x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.1 ms: 1.05x faster                                      |
| python_startup_no_site | 9.73 ms                                                | 9.88 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.55 ms: 1.39x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230522-darwin-arm64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 88.8 us: 3.87x faster                                      |
| deltablue                | 5.15 ms                                                | 2.60 ms: 1.98x faster                                      |
| richards_super           | 60.7 ms                                                | 34.8 ms: 1.74x faster                                      |
| logging_silent           | 119 ns                                                 | 68.9 ns: 1.73x faster                                      |
| richards                 | 51.4 ms                                                | 31.2 ms: 1.65x faster                                      |
| mypy2                    | 308 ms                                                 | 192 ms: 1.60x faster                                       |
| async_tree_memoization   | 493 ms                                                 | 310 ms: 1.59x faster                                       |
| go                       | 165 ms                                                 | 107 ms: 1.54x faster                                       |
| async_tree_none          | 402 ms                                                 | 263 ms: 1.53x faster                                       |
| async_tree_io            | 1.02 sec                                               | 668 ms: 1.53x faster                                       |
| pickle_pure_python       | 284 us                                                 | 188 us: 1.51x faster                                       |
| crypto_pyaes             | 78.0 ms                                                | 52.0 ms: 1.50x faster                                      |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.50x faster                                      |
| sqlglot_parse            | 1.33 ms                                                | 902 us: 1.48x faster                                       |
| asyncio_tcp              | 673 ms                                                 | 462 ms: 1.46x faster                                       |
| scimark_lu               | 110 ms                                                 | 75.5 ms: 1.46x faster                                      |
| chaos                    | 66.8 ms                                                | 46.4 ms: 1.44x faster                                      |
| sqlglot_transpile        | 1.54 ms                                                | 1.08 ms: 1.42x faster                                      |
| scimark_monte_carlo      | 72.2 ms                                                | 51.0 ms: 1.42x faster                                      |
| deepcopy_memo            | 34.5 us                                                | 24.6 us: 1.40x faster                                      |
| unpickle_pure_python     | 203 us                                                 | 146 us: 1.39x faster                                       |
| mako                     | 10.5 ms                                                | 7.55 ms: 1.39x faster                                      |
| nbody                    | 94.1 ms                                                | 68.6 ms: 1.37x faster                                      |
| pyflate                  | 453 ms                                                 | 332 ms: 1.37x faster                                       |
| pycparser                | 915 ms                                                 | 676 ms: 1.35x faster                                       |
| scimark_sor              | 127 ms                                                 | 94.5 ms: 1.34x faster                                      |
| unpack_sequence          | 38.7 ns                                                | 29.1 ns: 1.33x faster                                      |
| raytrace                 | 328 ms                                                 | 251 ms: 1.30x faster                                       |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.30x faster                                     |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.93 ms: 1.30x faster                                      |
| tornado_http             | 91.9 ms                                                | 71.4 ms: 1.29x faster                                      |
| json_dumps               | 8.38 ms                                                | 6.53 ms: 1.28x faster                                      |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 526 ms: 1.27x faster                                       |
| regex_compile            | 96.6 ms                                                | 75.9 ms: 1.27x faster                                      |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                     |
| spectral_norm            | 96.4 ms                                                | 76.3 ms: 1.26x faster                                      |
| create_gc_cycles         | 876 us                                                 | 700 us: 1.25x faster                                       |
| generators               | 32.9 ms                                                | 26.4 ms: 1.25x faster                                      |
| logging_format           | 5.01 us                                                | 4.03 us: 1.24x faster                                      |
| logging_simple           | 4.63 us                                                | 3.77 us: 1.23x faster                                      |
| dulwich_log              | 37.1 ms                                                | 30.2 ms: 1.23x faster                                      |
| deepcopy                 | 278 us                                                 | 227 us: 1.23x faster                                       |
| float                    | 72.3 ms                                                | 59.0 ms: 1.23x faster                                      |
| fannkuch                 | 317 ms                                                 | 261 ms: 1.21x faster                                       |
| pprint_pformat           | 1.24 sec                                               | 1.02 sec: 1.21x faster                                     |
| pprint_safe_repr         | 609 ms                                                 | 510 ms: 1.19x faster                                       |
| 2to3                     | 202 ms                                                 | 171 ms: 1.18x faster                                       |
| deepcopy_reduce          | 2.38 us                                                | 2.05 us: 1.17x faster                                      |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.16x faster                                       |
| docutils                 | 1.78 sec                                               | 1.55 sec: 1.15x faster                                     |
| xml_etree_process        | 45.1 ms                                                | 39.3 ms: 1.15x faster                                      |
| coroutines               | 20.2 ms                                                | 17.6 ms: 1.14x faster                                      |
| sqlalchemy_declarative   | 74.8 ms                                                | 66.0 ms: 1.13x faster                                      |
| nqueens                  | 68.1 ms                                                | 60.5 ms: 1.13x faster                                      |
| bench_thread_pool        | 548 us                                                 | 489 us: 1.12x faster                                       |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                      |
| comprehensions           | 17.7 us                                                | 16.0 us: 1.10x faster                                      |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.19 ms: 1.09x faster                                      |
| sqlglot_optimize         | 38.0 ms                                                | 35.0 ms: 1.09x faster                                      |
| meteor_contest           | 78.6 ms                                                | 73.4 ms: 1.07x faster                                      |
| regex_dna                | 160 ms                                                 | 150 ms: 1.06x faster                                       |
| unpickle                 | 9.77 us                                                | 9.30 us: 1.05x faster                                      |
| python_startup           | 12.6 ms                                                | 12.1 ms: 1.05x faster                                      |
| sqlglot_normalize        | 197 ms                                                 | 188 ms: 1.04x faster                                       |
| json                     | 3.10 ms                                                | 3.04 ms: 1.02x faster                                      |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                       |
| python_startup_no_site   | 9.73 ms                                                | 9.88 ms: 1.02x slower                                      |
| pickle                   | 7.36 us                                                | 7.49 us: 1.02x slower                                      |
| pathlib                  | 28.8 ms                                                | 29.7 ms: 1.03x slower                                      |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 72.6 ms                                                | 75.8 ms: 1.04x slower                                      |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| xml_etree_generate       | 54.3 ms                                                | 56.7 ms: 1.04x slower                                      |
| pickle_list              | 2.83 us                                                | 2.96 us: 1.05x slower                                      |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                      |
| telco                    | 3.68 ms                                                | 3.87 ms: 1.05x slower                                      |
| sqlite_synth             | 1.47 us                                                | 1.55 us: 1.05x slower                                      |
| pickle_dict              | 17.8 us                                                | 18.9 us: 1.07x slower                                      |
| bench_mp_pool            | 41.0 ms                                                | 45.9 ms: 1.12x slower                                      |
| unpickle_list            | 2.66 us                                                | 3.21 us: 1.21x slower                                      |
| coverage                 | 40.8 ms                                                | 51.4 ms: 1.26x slower                                      |
| dask                     | 258 ms                                                 | 331 ms: 1.28x slower                                       |
| async_generators         | 233 ms                                                 | 316 ms: 1.35x slower                                       |
| Geometric mean           | (ref)                                                  | 1.21x faster                                               |

Benchmark hidden because not significant (2): mdp, gc_traversal
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
