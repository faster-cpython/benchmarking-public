# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-aarch64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 365 ms: 1.04x faster                                                       |
| docutils       | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                     |
| html5lib       | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                      |
| tornado_http   | 178 ms                                                                | 138 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 433 ms: 2.19x faster                                                       |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 576 ms: 1.97x faster                                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 745 ms: 1.71x faster                                                       |
| Geometric mean          | (ref)                                                                 | 1.96x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.2 ms: 1.48x faster                                                      |
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                       |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                      |
| regex_compile  | 177 ms                                                                | 181 ms: 1.02x slower                                                       |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                                       |
| unpickle_pure_python | 366 us                                                                | 278 us: 1.31x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                      |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                      |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.07x faster                                                       |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                      |
| python_startup_no_site | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                      |
| django_template | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                      |
| genshi_text     | 35.2 ms                                                               | 36.5 ms: 1.04x slower                                                      |
| genshi_xml      | 69.8 ms                                                               | 82.9 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.13x faster                                                       |
| async_tree_none          | 950 ms                                                                | 433 ms: 2.19x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.46 ms: 2.01x faster                                                      |
| async_tree_memoization   | 1.13 sec                                                              | 576 ms: 1.97x faster                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 7.98 ms: 1.82x faster                                                      |
| generators               | 68.1 ms                                                               | 37.5 ms: 1.81x faster                                                      |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                       |
| richards_super           | 107 ms                                                                | 62.2 ms: 1.72x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 745 ms: 1.71x faster                                                       |
| richards                 | 91.7 ms                                                               | 55.2 ms: 1.66x faster                                                      |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                       |
| deepcopy_memo            | 61.7 us                                                               | 38.7 us: 1.59x faster                                                      |
| crypto_pyaes             | 134 ms                                                                | 87.4 ms: 1.53x faster                                                      |
| asyncio_tcp              | 944 ms                                                                | 626 ms: 1.51x faster                                                       |
| sqlglot_parse            | 2.40 ms                                                               | 1.62 ms: 1.49x faster                                                      |
| float                    | 135 ms                                                                | 91.2 ms: 1.48x faster                                                      |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                      |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                                       |
| go                       | 264 ms                                                                | 180 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 90.6 ms: 1.41x faster                                                      |
| comprehensions           | 33.1 us                                                               | 23.7 us: 1.40x faster                                                      |
| sqlglot_transpile        | 2.84 ms                                                               | 2.04 ms: 1.39x faster                                                      |
| scimark_sor              | 246 ms                                                                | 177 ms: 1.39x faster                                                       |
| chaos                    | 121 ms                                                                | 89.1 ms: 1.36x faster                                                      |
| deepcopy                 | 511 us                                                                | 381 us: 1.34x faster                                                       |
| logging_format           | 10.6 us                                                               | 7.92 us: 1.34x faster                                                      |
| logging_simple           | 9.78 us                                                               | 7.32 us: 1.34x faster                                                      |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 278 us: 1.31x faster                                                       |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.31x faster                                                       |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                      |
| tornado_http             | 178 ms                                                                | 138 ms: 1.29x faster                                                       |
| thrift                   | 1.26 ms                                                               | 983 us: 1.28x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                                     |
| pyflate                  | 795 ms                                                                | 631 ms: 1.26x faster                                                       |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                      |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                      |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.23x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                      |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                      |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                      |
| pycparser                | 1.69 sec                                                              | 1.41 sec: 1.20x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.11 ms: 1.20x faster                                                      |
| fannkuch                 | 546 ms                                                                | 469 ms: 1.16x faster                                                       |
| dask                     | 450 ms                                                                | 392 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.73 ms: 1.13x faster                                                      |
| pylint                   | 485 ms                                                                | 430 ms: 1.13x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                       |
| scimark_fft              | 500 ms                                                                | 458 ms: 1.09x faster                                                       |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.07x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 4.32 us: 1.06x faster                                                      |
| sqlglot_normalize        | 156 ms                                                                | 147 ms: 1.06x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                                     |
| django_template          | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 71.9 ms: 1.05x faster                                                      |
| 2to3                     | 381 ms                                                                | 365 ms: 1.04x faster                                                       |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                       |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                      |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.02x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.33 sec: 1.01x faster                                                     |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                      |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                       |
| sympy_integrate          | 26.5 ms                                                               | 26.8 ms: 1.01x slower                                                      |
| regex_compile            | 177 ms                                                                | 181 ms: 1.02x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.03x slower                                                      |
| sympy_str                | 329 ms                                                                | 341 ms: 1.04x slower                                                       |
| genshi_text              | 35.2 ms                                                               | 36.5 ms: 1.04x slower                                                      |
| docutils                 | 3.53 sec                                                              | 3.67 sec: 1.04x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                      |
| sympy_expand             | 543 ms                                                                | 580 ms: 1.07x slower                                                       |
| sympy_sum                | 184 ms                                                                | 197 ms: 1.07x slower                                                       |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                       |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                      |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                      |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                      |
| gc_traversal             | 4.15 ms                                                               | 4.91 ms: 1.18x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 82.9 ms: 1.19x slower                                                      |
| telco                    | 8.49 ms                                                               | 10.6 ms: 1.25x slower                                                      |
| python_startup_no_site   | 6.89 ms                                                               | 8.86 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_generate, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.23x