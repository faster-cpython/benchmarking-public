# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                         |
| chameleon      | 10.8 ms                                                               | 9.18 ms: 1.18x faster                                        |
| html5lib       | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                        |
| tornado_http   | 178 ms                                                                | 139 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 508 ms: 1.87x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 671 ms: 1.69x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 818 ms: 1.56x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.73x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.7 ms: 1.52x faster                                        |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                         |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                        |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.86 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                         |
| unpickle_pure_python | 366 us                                                                | 278 us: 1.32x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.12x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| unpickle_list        | 6.99 us                                                               | 6.58 us: 1.06x faster                                        |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.30 us: 1.01x slower                                        |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| pickle               | 12.5 us                                                               | 13.5 us: 1.09x slower                                        |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.3 ms: 1.37x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                        |
| django_template | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 83.4 ms: 1.19x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.58 ms: 1.95x faster                                        |
| async_tree_none          | 950 ms                                                                | 508 ms: 1.87x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                       |
| raytrace                 | 573 ms                                                                | 321 ms: 1.78x faster                                         |
| bench_mp_pool            | 14.5 ms                                                               | 8.24 ms: 1.76x faster                                        |
| generators               | 68.1 ms                                                               | 39.6 ms: 1.72x faster                                        |
| richards_super           | 107 ms                                                                | 63.4 ms: 1.69x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 671 ms: 1.69x faster                                         |
| richards                 | 91.7 ms                                                               | 56.2 ms: 1.63x faster                                        |
| logging_silent           | 222 ns                                                                | 141 ns: 1.58x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 818 ms: 1.56x faster                                         |
| asyncio_tcp              | 944 ms                                                                | 618 ms: 1.53x faster                                         |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.52x faster                                        |
| float                    | 135 ms                                                                | 88.7 ms: 1.52x faster                                        |
| crypto_pyaes             | 134 ms                                                                | 89.1 ms: 1.50x faster                                        |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                       |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 89.0 ms: 1.44x faster                                        |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                         |
| comprehensions           | 33.1 us                                                               | 23.2 us: 1.43x faster                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                        |
| scimark_sor              | 246 ms                                                                | 174 ms: 1.42x faster                                         |
| chaos                    | 121 ms                                                                | 87.1 ms: 1.39x faster                                        |
| logging_simple           | 9.78 us                                                               | 7.31 us: 1.34x faster                                        |
| pyflate                  | 795 ms                                                                | 596 ms: 1.33x faster                                         |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                         |
| logging_format           | 10.6 us                                                               | 8.05 us: 1.32x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 278 us: 1.32x faster                                         |
| thrift                   | 1.26 ms                                                               | 965 us: 1.31x faster                                         |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                        |
| tornado_http             | 178 ms                                                                | 139 ms: 1.29x faster                                         |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                       |
| spectral_norm            | 186 ms                                                                | 149 ms: 1.25x faster                                         |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                         |
| deepcopy_memo            | 61.7 us                                                               | 49.7 us: 1.24x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                        |
| hexiom                   | 10.9 ms                                                               | 8.89 ms: 1.23x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                        |
| html5lib                 | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                        |
| chameleon                | 10.8 ms                                                               | 9.18 ms: 1.18x faster                                        |
| fannkuch                 | 546 ms                                                                | 463 ms: 1.18x faster                                         |
| pylint                   | 485 ms                                                                | 414 ms: 1.17x faster                                         |
| dask                     | 450 ms                                                                | 393 ms: 1.14x faster                                         |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.12x faster                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.94 ms: 1.10x faster                                        |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.78 us: 1.09x faster                                        |
| aiohttp                  | 1.39 ms                                                               | 1.28 ms: 1.08x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 69.8 ms: 1.08x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.08x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                       |
| django_template          | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                        |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                         |
| gunicorn                 | 1.45 ms                                                               | 1.36 ms: 1.07x faster                                        |
| unpickle_list            | 6.99 us                                                               | 6.58 us: 1.06x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                        |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                         |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                         |
| sympy_integrate          | 26.5 ms                                                               | 25.5 ms: 1.04x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 71.0 ms: 1.03x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                       |
| sympy_str                | 329 ms                                                                | 321 ms: 1.02x faster                                         |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.31 sec: 1.02x faster                                       |
| deepcopy                 | 511 us                                                                | 502 us: 1.02x faster                                         |
| sympy_expand             | 543 ms                                                                | 538 ms: 1.01x faster                                         |
| sympy_sum                | 184 ms                                                                | 183 ms: 1.01x faster                                         |
| pickle_list              | 5.24 us                                                               | 5.30 us: 1.01x slower                                        |
| deepcopy_reduce          | 4.60 us                                                               | 4.68 us: 1.02x slower                                        |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 2.38 ms: 1.05x slower                                        |
| flaskblogging            | 4.83 ms                                                               | 5.16 ms: 1.07x slower                                        |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.09x slower                                        |
| async_generators         | 452 ms                                                                | 508 ms: 1.12x slower                                         |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.86 ms: 1.14x slower                                        |
| coverage                 | 83.6 ms                                                               | 98.1 ms: 1.17x slower                                        |
| genshi_xml               | 69.8 ms                                                               | 83.4 ms: 1.19x slower                                        |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 5.08 ms: 1.22x slower                                        |
| python_startup           | 11.2 ms                                                               | 15.3 ms: 1.37x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                 |

Benchmark hidden because not significant (7): regex_compile, mypy2, nqueens, pidigits, docutils, asyncio_websockets, genshi_text
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.24x