# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                              |
| docutils       | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                                            |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                             |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 443 ms: 2.15x faster                                                              |
| async_tree_io           | 2.28 sec                                                              | 1.09 sec: 2.09x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 558 ms: 2.03x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 736 ms: 1.73x faster                                                              |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                              |
| float          | 135 ms                                                                | 92.2 ms: 1.46x faster                                                             |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                             |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                                              |
| unpickle_pure_python | 366 us                                                                | 249 us: 1.47x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                             |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                             |
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                             |
| django_template | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                             |
| async_tree_none          | 950 ms                                                                | 443 ms: 2.15x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 1.09 sec: 2.09x faster                                                            |
| bench_mp_pool            | 14.5 ms                                                               | 7.07 ms: 2.06x faster                                                             |
| async_tree_memoization   | 1.13 sec                                                              | 558 ms: 2.03x faster                                                              |
| generators               | 68.1 ms                                                               | 34.9 ms: 1.95x faster                                                             |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                              |
| richards_super           | 107 ms                                                                | 58.9 ms: 1.82x faster                                                             |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                             |
| richards                 | 91.7 ms                                                               | 52.2 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 736 ms: 1.73x faster                                                              |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                              |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                                             |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                              |
| go                       | 264 ms                                                                | 158 ms: 1.67x faster                                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.66x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 83.0 ms: 1.61x faster                                                             |
| asyncio_tcp              | 944 ms                                                                | 585 ms: 1.61x faster                                                              |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 38.6 us: 1.60x faster                                                             |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                              |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                              |
| scimark_monte_carlo      | 128 ms                                                                | 83.0 ms: 1.54x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 7.22 ms: 1.51x faster                                                             |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                            |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                                              |
| unpickle_pure_python     | 366 us                                                                | 249 us: 1.47x faster                                                              |
| float                    | 135 ms                                                                | 92.2 ms: 1.46x faster                                                             |
| pyflate                  | 795 ms                                                                | 563 ms: 1.41x faster                                                              |
| logging_simple           | 9.78 us                                                               | 6.95 us: 1.41x faster                                                             |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                             |
| logging_format           | 10.6 us                                                               | 7.63 us: 1.39x faster                                                             |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                            |
| pylint                   | 485 ms                                                                | 355 ms: 1.37x faster                                                              |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.44 us: 1.34x faster                                                             |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                                              |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                                              |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                             |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                             |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.29x faster                                                             |
| django_template          | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                             |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                             |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                             |
| sympy_integrate          | 26.5 ms                                                               | 21.3 ms: 1.25x faster                                                             |
| dask                     | 450 ms                                                                | 364 ms: 1.23x faster                                                              |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                              |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                            |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 946 ms: 1.21x faster                                                              |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                                             |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.48 ms: 1.18x faster                                                             |
| fannkuch                 | 546 ms                                                                | 466 ms: 1.17x faster                                                              |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                              |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 62.2 ms: 1.12x faster                                                             |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                              |
| docutils                 | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                                            |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                            |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                             |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                             |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                              |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                                              |
| create_gc_cycles         | 2.26 ms                                                               | 2.32 ms: 1.03x slower                                                             |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                             |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                                              |
| telco                    | 8.49 ms                                                               | 9.76 ms: 1.15x slower                                                             |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                             |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                             |
| coverage                 | 83.6 ms                                                               | 98.0 ms: 1.17x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 5.04 ms: 1.21x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                                             |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                                      |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x