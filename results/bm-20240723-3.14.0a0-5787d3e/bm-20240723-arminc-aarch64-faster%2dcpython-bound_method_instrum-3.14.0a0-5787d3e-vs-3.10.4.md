# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-aarch64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                            |
| html5lib       | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                             |
| tornado_http   | 178 ms                                                                | 126 ms: 1.42x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 439 ms: 2.16x faster                                                              |
| async_tree_io           | 2.28 sec                                                              | 1.09 sec: 2.10x faster                                                            |
| async_tree_memoization  | 1.13 sec                                                              | 552 ms: 2.05x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 725 ms: 1.76x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.49x faster                                                              |
| float          | 135 ms                                                                | 92.3 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                              |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                             |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 355 us: 1.49x faster                                                              |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                            |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                             |
| xml_etree_process    | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                             |
| python_startup_no_site | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                             |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 198 us: 3.34x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.31x faster                                                             |
| async_tree_none          | 950 ms                                                                | 439 ms: 2.16x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 1.09 sec: 2.10x faster                                                            |
| async_tree_memoization   | 1.13 sec                                                              | 552 ms: 2.05x faster                                                              |
| bench_mp_pool            | 14.5 ms                                                               | 7.12 ms: 2.04x faster                                                             |
| generators               | 68.1 ms                                                               | 35.0 ms: 1.94x faster                                                             |
| raytrace                 | 573 ms                                                                | 298 ms: 1.92x faster                                                              |
| richards_super           | 107 ms                                                                | 58.9 ms: 1.82x faster                                                             |
| chaos                    | 121 ms                                                                | 67.7 ms: 1.79x faster                                                             |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 725 ms: 1.76x faster                                                              |
| logging_silent           | 222 ns                                                                | 130 ns: 1.70x faster                                                              |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                             |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                              |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                                              |
| asyncio_tcp              | 944 ms                                                                | 570 ms: 1.66x faster                                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.64x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.59x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.9 us: 1.58x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 81.9 ms: 1.56x faster                                                             |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                              |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                              |
| hexiom                   | 10.9 ms                                                               | 7.06 ms: 1.55x faster                                                             |
| pickle_pure_python       | 529 us                                                                | 355 us: 1.49x faster                                                              |
| nbody                    | 166 ms                                                                | 112 ms: 1.49x faster                                                              |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                            |
| float                    | 135 ms                                                                | 92.3 ms: 1.46x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                              |
| tornado_http             | 178 ms                                                                | 126 ms: 1.42x faster                                                              |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                             |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.40x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                            |
| pyflate                  | 795 ms                                                                | 576 ms: 1.38x faster                                                              |
| pylint                   | 485 ms                                                                | 352 ms: 1.38x faster                                                              |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                              |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.42 us: 1.35x faster                                                             |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                            |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                              |
| thrift                   | 1.26 ms                                                               | 954 us: 1.32x faster                                                              |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                             |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                             |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.29x faster                                                             |
| html5lib                 | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                             |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                             |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                             |
| dulwich_log              | 73.5 ms                                                               | 58.8 ms: 1.25x faster                                                             |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                                              |
| dask                     | 450 ms                                                                | 365 ms: 1.23x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 80.8 ms: 1.23x faster                                                             |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                                             |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 1.94 sec: 1.22x faster                                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 952 ms: 1.21x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.38 ms: 1.20x faster                                                             |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.18x faster                                                              |
| nqueens                  | 117 ms                                                                | 99.5 ms: 1.18x faster                                                             |
| fannkuch                 | 546 ms                                                                | 463 ms: 1.18x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                             |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                            |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                              |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                              |
| mdp                      | 3.70 sec                                                              | 3.37 sec: 1.10x faster                                                            |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                              |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                             |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 660 ms: 1.00x slower                                                              |
| create_gc_cycles         | 2.26 ms                                                               | 2.28 ms: 1.01x slower                                                             |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| async_generators         | 452 ms                                                                | 492 ms: 1.09x slower                                                              |
| telco                    | 8.49 ms                                                               | 9.60 ms: 1.13x slower                                                             |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                             |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 4.88 ms: 1.17x slower                                                             |
| coverage                 | 83.6 ms                                                               | 99.3 ms: 1.19x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                             |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                                      |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x