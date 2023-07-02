
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 18b1fde
- commit date: 2023-07-01
- overall geometric mean: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.57 sec: 1.13x faster                                |
| tornado_http   | 91.9 ms                                                | 72.8 ms: 1.26x faster                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 72.4 ms: 1.30x faster                                 |
| float          | 72.3 ms                                                | 60.0 ms: 1.20x faster                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 80.0 ms: 1.21x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 150 ms: 1.06x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 203 us: 1.40x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.66 ms: 1.26x faster                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 41.1 ms: 1.10x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.66 sec: 1.06x faster                                |
| unpickle             | 9.77 us                                                | 9.38 us: 1.04x faster                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| pickle_list          | 2.83 us                                                | 2.87 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 76.8 ms: 1.06x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 58.8 ms: 1.08x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.17 us: 1.19x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.9 ms: 1.16x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 8.81 ms: 1.10x faster                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.60 ms: 1.38x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-main-3.13.0a0-18b1fde |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 95.2 us: 3.62x faster                                 |
| deltablue                | 5.15 ms                                                | 2.88 ms: 1.79x faster                                 |
| chaos                    | 66.8 ms                                                | 42.2 ms: 1.58x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 438 ms: 1.54x faster                                  |
| logging_silent           | 119 ns                                                 | 77.7 ns: 1.53x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 325 ms: 1.52x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 52.5 ms: 1.49x faster                                 |
| richards_super           | 60.7 ms                                                | 41.2 ms: 1.47x faster                                 |
| async_tree_io            | 1.02 sec                                               | 693 ms: 1.47x faster                                  |
| raytrace                 | 328 ms                                                 | 224 ms: 1.46x faster                                  |
| async_tree_none          | 402 ms                                                 | 276 ms: 1.46x faster                                  |
| scimark_lu               | 110 ms                                                 | 75.6 ms: 1.45x faster                                 |
| sqlglot_parse            | 1.33 ms                                                | 954 us: 1.40x faster                                  |
| pickle_pure_python       | 284 us                                                 | 203 us: 1.40x faster                                  |
| mako                     | 10.5 ms                                                | 7.60 ms: 1.38x faster                                 |
| richards                 | 51.4 ms                                                | 37.4 ms: 1.37x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 28.2 ns: 1.37x faster                                 |
| go                       | 165 ms                                                 | 122 ms: 1.35x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.14 ms: 1.35x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.72 ms: 1.34x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 26.2 us: 1.32x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                |
| nbody                    | 94.1 ms                                                | 72.4 ms: 1.30x faster                                 |
| pycparser                | 915 ms                                                 | 710 ms: 1.29x faster                                  |
| spectral_norm            | 96.4 ms                                                | 75.2 ms: 1.28x faster                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 56.7 ms: 1.27x faster                                 |
| tornado_http             | 91.9 ms                                                | 72.8 ms: 1.26x faster                                 |
| json_dumps               | 8.38 ms                                                | 6.66 ms: 1.26x faster                                 |
| create_gc_cycles         | 876 us                                                 | 697 us: 1.26x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 162 us: 1.26x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 539 ms: 1.24x faster                                  |
| pyflate                  | 453 ms                                                 | 373 ms: 1.21x faster                                  |
| generators               | 32.9 ms                                                | 27.2 ms: 1.21x faster                                 |
| regex_compile            | 96.6 ms                                                | 80.0 ms: 1.21x faster                                 |
| float                    | 72.3 ms                                                | 60.0 ms: 1.20x faster                                 |
| dulwich_log              | 37.1 ms                                                | 30.8 ms: 1.20x faster                                 |
| logging_format           | 5.01 us                                                | 4.24 us: 1.18x faster                                 |
| deepcopy                 | 278 us                                                 | 235 us: 1.18x faster                                  |
| logging_simple           | 4.63 us                                                | 3.94 us: 1.17x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.06 sec: 1.17x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 522 ms: 1.17x faster                                  |
| mypy2                    | 308 ms                                                 | 265 ms: 1.16x faster                                  |
| python_startup           | 12.6 ms                                                | 10.9 ms: 1.16x faster                                 |
| docutils                 | 1.78 sec                                               | 1.57 sec: 1.13x faster                                |
| scimark_fft              | 232 ms                                                 | 205 ms: 1.13x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.12 us: 1.12x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| nqueens                  | 68.1 ms                                                | 61.5 ms: 1.11x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 8.81 ms: 1.10x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 41.1 ms: 1.10x faster                                 |
| bench_thread_pool        | 548 us                                                 | 501 us: 1.09x faster                                  |
| fannkuch                 | 317 ms                                                 | 291 ms: 1.09x faster                                  |
| comprehensions           | 17.7 us                                                | 16.4 us: 1.08x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 35.3 ms: 1.08x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.23 ms: 1.08x faster                                 |
| scimark_sor              | 127 ms                                                 | 119 ms: 1.06x faster                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.06x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.66 sec: 1.06x faster                                |
| coroutines               | 20.2 ms                                                | 19.3 ms: 1.05x faster                                 |
| unpickle                 | 9.77 us                                                | 9.38 us: 1.04x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                 |
| meteor_contest           | 78.6 ms                                                | 76.6 ms: 1.03x faster                                 |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| mdp                      | 1.67 sec                                               | 1.68 sec: 1.01x slower                                |
| pickle_list              | 2.83 us                                                | 2.87 us: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 76.8 ms: 1.06x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 58.8 ms: 1.08x slower                                 |
| pathlib                  | 28.8 ms                                                | 31.4 ms: 1.09x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 44.8 ms: 1.09x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.62 us: 1.10x slower                                 |
| telco                    | 3.68 ms                                                | 4.25 ms: 1.15x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.17 us: 1.19x slower                                 |
| coverage                 | 40.8 ms                                                | 51.3 ms: 1.26x slower                                 |
| async_generators         | 233 ms                                                 | 313 ms: 1.34x slower                                  |
| Geometric mean           | (ref)                                                  | 1.18x faster                                          |

Benchmark hidden because not significant (2): pidigits, pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
