# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 356 ms: 1.07x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.7 ms: 1.22x faster                                                  |
| tornado_http   | 178 ms                                                                | 138 ms: 1.29x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 494 ms: 1.92x faster                                                   |
| async_tree_io           | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                 |
| async_tree_memoization  | 1.13 sec                                                              | 665 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 799 ms: 1.59x faster                                                   |
| Geometric mean          | (ref)                                                                 | 1.77x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.1 ms: 1.49x faster                                                  |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                  |
| regex_dna      | 257 ms                                                                | 258 ms: 1.00x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 275 us: 1.33x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.29x faster                                                 |
| pickle_pure_python   | 529 us                                                                | 413 us: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.67 us: 1.05x faster                                                  |
| pickle_list          | 5.24 us                                                               | 5.27 us: 1.01x slower                                                  |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                  |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                                  |
| pickle               | 12.5 us                                                               | 13.4 us: 1.07x slower                                                  |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.8 ms: 1.14x slower                                                  |
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                  |
| django_template | 53.3 ms                                                               | 49.1 ms: 1.09x faster                                                  |
| genshi_text     | 35.2 ms                                                               | 34.0 ms: 1.03x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.18x faster                                                   |
| deltablue                | 8.94 ms                                                               | 4.61 ms: 1.94x faster                                                  |
| async_tree_none          | 950 ms                                                                | 494 ms: 1.92x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.22 sec: 1.87x faster                                                 |
| bench_mp_pool            | 14.5 ms                                                               | 8.01 ms: 1.81x faster                                                  |
| generators               | 68.1 ms                                                               | 38.2 ms: 1.78x faster                                                  |
| raytrace                 | 573 ms                                                                | 325 ms: 1.77x faster                                                   |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 665 ms: 1.70x faster                                                   |
| richards                 | 91.7 ms                                                               | 55.4 ms: 1.66x faster                                                  |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 799 ms: 1.59x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 88.8 ms: 1.51x faster                                                  |
| asyncio_tcp              | 944 ms                                                                | 630 ms: 1.50x faster                                                   |
| float                    | 135 ms                                                                | 90.1 ms: 1.49x faster                                                  |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                   |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                  |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                                 |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.44x faster                                                  |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 90.6 ms: 1.41x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 2.03 ms: 1.40x faster                                                  |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                   |
| chaos                    | 121 ms                                                                | 88.2 ms: 1.37x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.89 us: 1.35x faster                                                  |
| thrift                   | 1.26 ms                                                               | 944 us: 1.33x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.35 us: 1.33x faster                                                  |
| pyflate                  | 795 ms                                                                | 598 ms: 1.33x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 275 us: 1.33x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.29x faster                                                 |
| tornado_http             | 178 ms                                                                | 138 ms: 1.29x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 413 us: 1.28x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 48.8 us: 1.26x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                                 |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                  |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.7 ms: 1.22x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 8.96 ms: 1.22x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.18x faster                                                  |
| dask                     | 450 ms                                                                | 390 ms: 1.15x faster                                                   |
| pylint                   | 485 ms                                                                | 421 ms: 1.15x faster                                                   |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.94 ms: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 69.1 ms: 1.09x faster                                                  |
| scimark_fft              | 500 ms                                                                | 460 ms: 1.09x faster                                                   |
| django_template          | 53.3 ms                                                               | 49.1 ms: 1.09x faster                                                  |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                                 |
| regex_v8                 | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                  |
| 2to3                     | 381 ms                                                                | 356 ms: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.92 us: 1.05x faster                                                  |
| unpickle_list            | 6.99 us                                                               | 6.67 us: 1.05x faster                                                  |
| deepcopy                 | 511 us                                                                | 490 us: 1.04x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 70.6 ms: 1.04x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 34.0 ms: 1.03x faster                                                  |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                  |
| sympy_str                | 329 ms                                                                | 319 ms: 1.03x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.03x faster                                                 |
| sympy_integrate          | 26.5 ms                                                               | 25.9 ms: 1.02x faster                                                  |
| sympy_expand             | 543 ms                                                                | 534 ms: 1.02x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.01x faster                                                 |
| regex_dna                | 257 ms                                                                | 258 ms: 1.00x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.27 us: 1.01x slower                                                  |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.65 us: 1.01x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                  |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                  |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                  |
| pickle                   | 12.5 us                                                               | 13.4 us: 1.07x slower                                                  |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.11x slower                                                  |
| async_generators         | 452 ms                                                                | 512 ms: 1.13x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.8 ms: 1.14x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                  |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                  |
| telco                    | 8.49 ms                                                               | 9.98 ms: 1.18x slower                                                  |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.18 ms: 1.25x slower                                                  |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                           |

Benchmark hidden because not significant (5): nqueens, regex_compile, pidigits, docutils, sympy_sum
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.22x