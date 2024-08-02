# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 364 ms: 1.05x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.32 ms: 1.16x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.7 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 144 ms: 1.24x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 499 ms: 1.90x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.24 sec: 1.84x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 656 ms: 1.73x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 801 ms: 1.59x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.76x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_compile  | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.95 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 276 us: 1.32x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.35 us: 1.10x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.03x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| pickle               | 12.5 us                                                               | 14.1 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 10.8 ms: 1.57x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 81.9 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.56 ms: 1.96x faster                                                   |
| async_tree_none          | 950 ms                                                                | 499 ms: 1.90x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.24 sec: 1.84x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 8.24 ms: 1.76x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| generators               | 68.1 ms                                                               | 38.7 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.3 ms: 1.75x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 656 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.1 ms: 1.69x faster                                                   |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 801 ms: 1.59x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 605 ms: 1.56x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 87.0 ms: 1.54x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                   |
| float                    | 135 ms                                                                | 90.6 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.4 ms: 1.46x faster                                                   |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| comprehensions           | 33.1 us                                                               | 22.9 us: 1.45x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.44x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.04 ms: 1.39x faster                                                   |
| chaos                    | 121 ms                                                                | 88.7 ms: 1.37x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.92 us: 1.34x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 276 us: 1.32x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.39 us: 1.32x faster                                                   |
| thrift                   | 1.26 ms                                                               | 966 us: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.28x faster                                                  |
| pyflate                  | 795 ms                                                                | 619 ms: 1.28x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| scimark_lu               | 227 ms                                                                | 182 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| tornado_http             | 178 ms                                                                | 144 ms: 1.24x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.1 us: 1.23x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.7 ms: 1.22x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 8.99 ms: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                   |
| chameleon                | 10.8 ms                                                               | 9.32 ms: 1.16x faster                                                   |
| pylint                   | 485 ms                                                                | 419 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                   |
| dask                     | 450 ms                                                                | 397 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.84 ms: 1.12x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.35 us: 1.10x faster                                                   |
| scimark_fft              | 500 ms                                                                | 455 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 69.9 ms: 1.08x faster                                                   |
| django_template          | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                   |
| meteor_contest           | 126 ms                                                                | 119 ms: 1.06x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| 2to3                     | 381 ms                                                                | 364 ms: 1.05x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.04x faster                                                  |
| regex_compile            | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                   |
| deepcopy                 | 511 us                                                                | 495 us: 1.03x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.29 sec: 1.03x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.03x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 71.8 ms: 1.02x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 26.4 ms: 1.01x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                  |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.67 us: 1.02x slower                                                   |
| sympy_expand             | 543 ms                                                                | 554 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| flaskblogging            | 4.83 ms                                                               | 5.12 ms: 1.06x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.49 ms: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| pickle                   | 12.5 us                                                               | 14.1 us: 1.13x slower                                                   |
| async_generators         | 452 ms                                                                | 513 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.95 ms: 1.16x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 81.9 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.35 ms: 1.29x slower                                                   |
| python_startup           | 11.2 ms                                                               | 14.8 ms: 1.33x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 10.8 ms: 1.57x slower                                                   |
| telco                    | 8.49 ms                                                               | 166 ms: 19.51x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.15x faster                                                            |

Benchmark hidden because not significant (4): sympy_str, pidigits, nqueens, sympy_sum
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.25x