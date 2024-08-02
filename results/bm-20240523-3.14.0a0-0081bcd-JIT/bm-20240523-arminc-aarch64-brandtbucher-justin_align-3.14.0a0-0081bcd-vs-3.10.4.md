# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: linux-aarch64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 353 ms: 1.08x faster                                                  |
| chameleon      | 10.8 ms                                                               | 9.09 ms: 1.19x faster                                                 |
| html5lib       | 86.5 ms                                                               | 70.4 ms: 1.23x faster                                                 |
| tornado_http   | 178 ms                                                                | 138 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 509 ms: 1.87x faster                                                  |
| async_tree_io           | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 676 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 831 ms: 1.53x faster                                                  |
| Geometric mean          | (ref)                                                                 | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.0 ms: 1.48x faster                                                 |
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 165 ms: 1.07x faster                                                  |
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                 |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                  |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 272 us: 1.34x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 403 us: 1.31x faster                                                  |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                 |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.10x faster                                                  |
| unpickle_list        | 6.99 us                                                               | 6.35 us: 1.10x faster                                                 |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                  |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                 |
| pickle_dict          | 35.1 us                                                               | 37.4 us: 1.07x slower                                                 |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                 |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 14.9 ms: 1.33x slower                                                 |
| python_startup_no_site | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.6 ms: 1.50x faster                                                 |
| django_template | 53.3 ms                                                               | 49.3 ms: 1.08x faster                                                 |
| genshi_text     | 35.2 ms                                                               | 33.2 ms: 1.06x faster                                                 |
| genshi_xml      | 69.8 ms                                                               | 80.0 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.24x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.57 ms: 1.96x faster                                                 |
| async_tree_none          | 950 ms                                                                | 509 ms: 1.87x faster                                                  |
| async_tree_io            | 2.28 sec                                                              | 1.26 sec: 1.81x faster                                                |
| raytrace                 | 573 ms                                                                | 321 ms: 1.79x faster                                                  |
| richards_super           | 107 ms                                                                | 60.2 ms: 1.78x faster                                                 |
| generators               | 68.1 ms                                                               | 38.5 ms: 1.77x faster                                                 |
| bench_mp_pool            | 14.5 ms                                                               | 8.28 ms: 1.76x faster                                                 |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                 |
| async_tree_memoization   | 1.13 sec                                                              | 676 ms: 1.68x faster                                                  |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 86.7 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 831 ms: 1.53x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.53x faster                                                 |
| go                       | 264 ms                                                                | 176 ms: 1.50x faster                                                  |
| asyncio_tcp              | 944 ms                                                                | 629 ms: 1.50x faster                                                  |
| mako                     | 18.9 ms                                                               | 12.6 ms: 1.50x faster                                                 |
| float                    | 135 ms                                                                | 91.0 ms: 1.48x faster                                                 |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                                  |
| comprehensions           | 33.1 us                                                               | 23.0 us: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.44x faster                                                |
| scimark_monte_carlo      | 128 ms                                                                | 90.0 ms: 1.42x faster                                                 |
| chaos                    | 121 ms                                                                | 85.6 ms: 1.41x faster                                                 |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                 |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.40x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.22 us: 1.35x faster                                                 |
| unpickle_pure_python     | 366 us                                                                | 272 us: 1.34x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.89 us: 1.34x faster                                                 |
| pickle_pure_python       | 529 us                                                                | 403 us: 1.31x faster                                                  |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.30x faster                                                  |
| pyflate                  | 795 ms                                                                | 613 ms: 1.30x faster                                                  |
| thrift                   | 1.26 ms                                                               | 975 us: 1.29x faster                                                  |
| tornado_http             | 178 ms                                                                | 138 ms: 1.29x faster                                                  |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                 |
| deepcopy_memo            | 61.7 us                                                               | 48.7 us: 1.27x faster                                                 |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                 |
| scimark_lu               | 227 ms                                                                | 179 ms: 1.26x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                |
| hexiom                   | 10.9 ms                                                               | 8.67 ms: 1.26x faster                                                 |
| fannkuch                 | 546 ms                                                                | 437 ms: 1.25x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                 |
| html5lib                 | 86.5 ms                                                               | 70.4 ms: 1.23x faster                                                 |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                 |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                 |
| chameleon                | 10.8 ms                                                               | 9.09 ms: 1.19x faster                                                 |
| pylint                   | 485 ms                                                                | 415 ms: 1.17x faster                                                  |
| dask                     | 450 ms                                                                | 393 ms: 1.15x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.87 ms: 1.11x faster                                                 |
| scimark_fft              | 500 ms                                                                | 451 ms: 1.11x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.10x faster                                                  |
| unpickle_list            | 6.99 us                                                               | 6.35 us: 1.10x faster                                                 |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 68.9 ms: 1.09x faster                                                 |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                  |
| django_template          | 53.3 ms                                                               | 49.3 ms: 1.08x faster                                                 |
| 2to3                     | 381 ms                                                                | 353 ms: 1.08x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                                 |
| regex_compile            | 177 ms                                                                | 165 ms: 1.07x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 1.07 sec: 1.07x faster                                                |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                |
| pprint_pformat           | 2.36 sec                                                              | 2.22 sec: 1.06x faster                                                |
| genshi_text              | 35.2 ms                                                               | 33.2 ms: 1.06x faster                                                 |
| dulwich_log              | 73.5 ms                                                               | 69.5 ms: 1.06x faster                                                 |
| sympy_str                | 329 ms                                                                | 313 ms: 1.05x faster                                                  |
| json                     | 5.88 ms                                                               | 5.62 ms: 1.05x faster                                                 |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                  |
| deepcopy                 | 511 us                                                                | 492 us: 1.04x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 25.6 ms: 1.04x faster                                                 |
| nqueens                  | 117 ms                                                                | 114 ms: 1.03x faster                                                  |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                  |
| sympy_expand             | 543 ms                                                                | 532 ms: 1.02x faster                                                  |
| sympy_sum                | 184 ms                                                                | 181 ms: 1.02x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                  |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                 |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                                 |
| pickle_dict              | 35.1 us                                                               | 37.4 us: 1.07x slower                                                 |
| flaskblogging            | 4.83 ms                                                               | 5.23 ms: 1.08x slower                                                 |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                 |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                 |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 80.0 ms: 1.15x slower                                                 |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                 |
| telco                    | 8.49 ms                                                               | 9.90 ms: 1.17x slower                                                 |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 5.27 ms: 1.27x slower                                                 |
| python_startup           | 11.2 ms                                                               | 14.9 ms: 1.33x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                          |

Benchmark hidden because not significant (4): pidigits, pickle_list, deepcopy_reduce, docutils
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-arminc-aarch64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.24x