# Results vs. 3.10.4

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: linux-aarch64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 361 ms: 1.06x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.28 ms: 1.17x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.29x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 517 ms: 1.84x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 684 ms: 1.66x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 825 ms: 1.54x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.71x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.4 ms: 1.47x faster                                                   |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_compile  | 177 ms                                                                | 172 ms: 1.03x faster                                                    |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 278 us: 1.32x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 10.8 ms: 1.57x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.44x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                   |
| django_template | 53.3 ms                                                               | 51.5 ms: 1.04x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 83.8 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.17x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.62 ms: 1.94x faster                                                   |
| async_tree_none          | 950 ms                                                                | 517 ms: 1.84x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 8.11 ms: 1.79x faster                                                   |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 38.6 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                   |
| richards                 | 91.7 ms                                                               | 54.7 ms: 1.68x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 684 ms: 1.66x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.58x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 825 ms: 1.54x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 617 ms: 1.53x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 90.7 ms: 1.48x faster                                                   |
| float                    | 135 ms                                                                | 91.4 ms: 1.47x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.47x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.43x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.42x faster                                                   |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 92.8 ms: 1.38x faster                                                   |
| chaos                    | 121 ms                                                                | 88.8 ms: 1.36x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.32 us: 1.34x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.99 us: 1.33x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 278 us: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 972 us: 1.30x faster                                                    |
| tornado_http             | 178 ms                                                                | 139 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| pyflate                  | 795 ms                                                                | 633 ms: 1.26x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 50.0 us: 1.23x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.4 ms: 1.21x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.07 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| pylint                   | 485 ms                                                                | 413 ms: 1.18x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.28 ms: 1.17x faster                                                   |
| dask                     | 450 ms                                                                | 389 ms: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 461 ms: 1.09x faster                                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.08x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 70.3 ms: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                                   |
| 2to3                     | 381 ms                                                                | 361 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                  |
| django_template          | 53.3 ms                                                               | 51.5 ms: 1.04x faster                                                   |
| regex_compile            | 177 ms                                                                | 172 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.03x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 71.9 ms: 1.02x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 26.0 ms: 1.02x faster                                                   |
| sympy_str                | 329 ms                                                                | 323 ms: 1.02x faster                                                    |
| deepcopy                 | 511 us                                                                | 503 us: 1.01x faster                                                    |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                  |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.72 us: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| flaskblogging            | 4.83 ms                                                               | 5.12 ms: 1.06x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.42 ms: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| async_generators         | 452 ms                                                                | 511 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.6 ms: 1.19x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 83.8 ms: 1.20x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.10 ms: 1.23x slower                                                   |
| python_startup           | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 10.8 ms: 1.57x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_iterparse, pickle_list, sympy_expand, pidigits, sympy_sum, genshi_text
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.24x