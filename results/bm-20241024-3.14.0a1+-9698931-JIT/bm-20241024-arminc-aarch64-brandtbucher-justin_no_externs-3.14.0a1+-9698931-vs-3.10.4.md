# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.117x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 401 ms: 1.05x slower                                                        |
| docutils       | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                      |
| html5lib       | 86.5 ms                                                               | 73.0 ms: 1.18x faster                                                       |
| tornado_http   | 178 ms                                                                | 152 ms: 1.18x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 473 ms: 2.01x faster                                                        |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                      |
| async_tree_memoization  | 1.13 sec                                                              | 606 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 768 ms: 1.66x faster                                                        |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 98.7 ms: 1.37x faster                                                       |
| nbody          | 166 ms                                                                | 132 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                       |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                        |
| regex_compile  | 177 ms                                                                | 183 ms: 1.04x slower                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                        |
| pickle_pure_python   | 529 us                                                                | 411 us: 1.29x faster                                                        |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                       |
| xml_etree_process    | 99.5 ms                                                               | 86.3 ms: 1.15x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                      |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.03x faster                                                        |
| json_loads           | 30.9 us                                                               | 31.8 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                       |
| python_startup         | 11.2 ms                                                               | 14.6 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                       |
| django_template | 53.3 ms                                                               | 55.3 ms: 1.04x slower                                                       |
| genshi_xml      | 69.8 ms                                                               | 86.4 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 221 us: 2.99x faster                                                        |
| async_tree_none          | 950 ms                                                                | 473 ms: 2.01x faster                                                        |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.91x faster                                                      |
| async_tree_memoization   | 1.13 sec                                                              | 606 ms: 1.87x faster                                                        |
| deltablue                | 8.94 ms                                                               | 4.83 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 768 ms: 1.66x faster                                                        |
| raytrace                 | 573 ms                                                                | 368 ms: 1.56x faster                                                        |
| scimark_sor              | 246 ms                                                                | 166 ms: 1.49x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 42.3 us: 1.46x faster                                                       |
| logging_silent           | 222 ns                                                                | 153 ns: 1.45x faster                                                        |
| scimark_lu               | 227 ms                                                                | 158 ms: 1.44x faster                                                        |
| float                    | 135 ms                                                                | 98.7 ms: 1.37x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 99.1 ms: 1.35x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                        |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                                       |
| richards_super           | 107 ms                                                                | 80.8 ms: 1.33x faster                                                       |
| sqlglot_parse            | 2.40 ms                                                               | 1.82 ms: 1.32x faster                                                       |
| go                       | 264 ms                                                                | 203 ms: 1.30x faster                                                        |
| deepcopy                 | 511 us                                                                | 392 us: 1.30x faster                                                        |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                       |
| thrift                   | 1.26 ms                                                               | 971 us: 1.30x faster                                                        |
| pickle_pure_python       | 529 us                                                                | 411 us: 1.29x faster                                                        |
| logging_simple           | 9.78 us                                                               | 7.63 us: 1.28x faster                                                       |
| logging_format           | 10.6 us                                                               | 8.34 us: 1.27x faster                                                       |
| chaos                    | 121 ms                                                                | 95.6 ms: 1.27x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 101 ms: 1.26x faster                                                        |
| nbody                    | 166 ms                                                                | 132 ms: 1.26x faster                                                        |
| generators               | 68.1 ms                                                               | 55.2 ms: 1.23x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 2.33 ms: 1.22x faster                                                       |
| comprehensions           | 33.1 us                                                               | 27.3 us: 1.22x faster                                                       |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 73.0 ms: 1.18x faster                                                       |
| tornado_http             | 178 ms                                                                | 152 ms: 1.18x faster                                                        |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                       |
| xml_etree_process        | 99.5 ms                                                               | 86.3 ms: 1.15x faster                                                       |
| richards                 | 91.7 ms                                                               | 79.8 ms: 1.15x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.93 sec: 1.15x faster                                                      |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                        |
| spectral_norm            | 186 ms                                                                | 167 ms: 1.11x faster                                                        |
| pylint                   | 485 ms                                                                | 438 ms: 1.11x faster                                                        |
| deepcopy_reduce          | 4.60 us                                                               | 4.19 us: 1.10x faster                                                       |
| pyflate                  | 795 ms                                                                | 725 ms: 1.10x faster                                                        |
| pycparser                | 1.69 sec                                                              | 1.58 sec: 1.07x faster                                                      |
| sqlalchemy_imperative    | 20.5 ms                                                               | 19.2 ms: 1.07x faster                                                       |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                        |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.55 sec: 1.04x faster                                                      |
| scimark_fft              | 500 ms                                                                | 481 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.03x faster                                                        |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                        |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                       |
| sqlalchemy_declarative   | 197 ms                                                                | 193 ms: 1.02x faster                                                        |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                        |
| json_loads               | 30.9 us                                                               | 31.8 us: 1.03x slower                                                       |
| django_template          | 53.3 ms                                                               | 55.3 ms: 1.04x slower                                                       |
| regex_compile            | 177 ms                                                                | 183 ms: 1.04x slower                                                        |
| sqlglot_normalize        | 156 ms                                                                | 163 ms: 1.05x slower                                                        |
| hexiom                   | 10.9 ms                                                               | 11.5 ms: 1.05x slower                                                       |
| 2to3                     | 381 ms                                                                | 401 ms: 1.05x slower                                                        |
| meteor_contest           | 126 ms                                                                | 133 ms: 1.06x slower                                                        |
| docutils                 | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                      |
| dulwich_log              | 73.5 ms                                                               | 81.7 ms: 1.11x slower                                                       |
| sympy_expand             | 543 ms                                                                | 603 ms: 1.11x slower                                                        |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                        |
| sympy_str                | 329 ms                                                                | 370 ms: 1.13x slower                                                        |
| sympy_integrate          | 26.5 ms                                                               | 30.3 ms: 1.14x slower                                                       |
| sqlglot_optimize         | 75.4 ms                                                               | 86.1 ms: 1.14x slower                                                       |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                       |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                       |
| nqueens                  | 117 ms                                                                | 139 ms: 1.18x slower                                                        |
| coverage                 | 83.6 ms                                                               | 98.8 ms: 1.18x slower                                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 1.37 sec: 1.19x slower                                                      |
| sympy_sum                | 184 ms                                                                | 222 ms: 1.21x slower                                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.85 sec: 1.21x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 86.4 ms: 1.24x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                       |
| python_startup           | 11.2 ms                                                               | 14.6 ms: 1.30x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 6.16 ms: 1.48x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.67 ms: 1.62x slower                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 2.46 sec: 169.24x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.05x faster                                                                |

Benchmark hidden because not significant (4): pidigits, genshi_text, fannkuch, scimark_sparse_mat_mult
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.117x faster
# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.38x