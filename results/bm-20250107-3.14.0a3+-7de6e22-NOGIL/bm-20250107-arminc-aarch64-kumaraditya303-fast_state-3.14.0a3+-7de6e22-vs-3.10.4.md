# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.058x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 463 ms: 1.22x slower                                                   |
| docutils       | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                 |
| html5lib       | 86.5 ms                                                               | 108 ms: 1.25x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                 |
| async_tree_none         | 950 ms                                                                | 540 ms: 1.76x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 655 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 833 ms: 1.53x faster                                                   |
| Geometric mean          | (ref)                                                                 | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 182 ms: 1.10x slower                                                   |
| float          | 135 ms                                                                | 154 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 274 ms: 1.06x slower                                                   |
| regex_compile  | 177 ms                                                                | 191 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 135 ms: 1.15x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 3.56 sec: 1.06x slower                                                 |
| json_dumps           | 16.7 ms                                                               | 18.1 ms: 1.09x slower                                                  |
| xml_etree_process    | 99.5 ms                                                               | 111 ms: 1.11x slower                                                   |
| json_loads           | 30.9 us                                                               | 36.0 us: 1.16x slower                                                  |
| xml_etree_generate   | 123 ms                                                                | 143 ms: 1.16x slower                                                   |
| unpickle_pure_python | 366 us                                                                | 455 us: 1.25x slower                                                   |
| pickle_pure_python   | 529 us                                                                | 702 us: 1.33x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.5 ms: 1.81x slower                                                  |
| python_startup         | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.82x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 40.5 ms: 1.15x slower                                                  |
| genshi_xml      | 69.8 ms                                                               | 81.2 ms: 1.16x slower                                                  |
| django_template | 53.3 ms                                                               | 66.8 ms: 1.25x slower                                                  |
| mako            | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 288 us: 2.30x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                 |
| async_tree_none          | 950 ms                                                                | 540 ms: 1.76x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 655 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 833 ms: 1.53x faster                                                   |
| generators               | 68.1 ms                                                               | 55.9 ms: 1.22x faster                                                  |
| spectral_norm            | 186 ms                                                                | 156 ms: 1.20x faster                                                   |
| deepcopy                 | 511 us                                                                | 443 us: 1.15x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 135 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 121 ms: 1.11x faster                                                   |
| coroutines               | 37.2 ms                                                               | 33.5 ms: 1.11x faster                                                  |
| pylint                   | 485 ms                                                                | 442 ms: 1.10x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 56.9 us: 1.08x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 24.3 ms: 1.08x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                                  |
| chaos                    | 121 ms                                                                | 127 ms: 1.05x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 688 ms: 1.05x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 3.56 sec: 1.06x slower                                                 |
| docutils                 | 3.53 sec                                                              | 3.74 sec: 1.06x slower                                                 |
| json                     | 5.88 ms                                                               | 6.23 ms: 1.06x slower                                                  |
| regex_dna                | 257 ms                                                                | 274 ms: 1.06x slower                                                   |
| richards                 | 91.7 ms                                                               | 97.7 ms: 1.07x slower                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.90 us: 1.07x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.15 ms: 1.07x slower                                                  |
| regex_compile            | 177 ms                                                                | 191 ms: 1.08x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 18.1 ms: 1.09x slower                                                  |
| mdp                      | 3.70 sec                                                              | 4.03 sec: 1.09x slower                                                 |
| nbody                    | 166 ms                                                                | 182 ms: 1.10x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.39 ms: 1.10x slower                                                  |
| xml_etree_process        | 99.5 ms                                                               | 111 ms: 1.11x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 29.8 ms: 1.12x slower                                                  |
| sqlglot_normalize        | 156 ms                                                                | 176 ms: 1.13x slower                                                   |
| pyflate                  | 795 ms                                                                | 901 ms: 1.13x slower                                                   |
| logging_simple           | 9.78 us                                                               | 11.1 us: 1.14x slower                                                  |
| sympy_sum                | 184 ms                                                                | 210 ms: 1.14x slower                                                   |
| float                    | 135 ms                                                                | 154 ms: 1.14x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 86.6 ms: 1.15x slower                                                  |
| raytrace                 | 573 ms                                                                | 658 ms: 1.15x slower                                                   |
| comprehensions           | 33.1 us                                                               | 38.1 us: 1.15x slower                                                  |
| logging_silent           | 222 ns                                                                | 255 ns: 1.15x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 40.5 ms: 1.15x slower                                                  |
| nqueens                  | 117 ms                                                                | 136 ms: 1.16x slower                                                   |
| sympy_str                | 329 ms                                                                | 381 ms: 1.16x slower                                                   |
| logging_format           | 10.6 us                                                               | 12.3 us: 1.16x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 81.2 ms: 1.16x slower                                                  |
| json_loads               | 30.9 us                                                               | 36.0 us: 1.16x slower                                                  |
| xml_etree_generate       | 123 ms                                                                | 143 ms: 1.16x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.76 sec: 1.17x slower                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 1.34 sec: 1.17x slower                                                 |
| scimark_sor              | 246 ms                                                                | 289 ms: 1.17x slower                                                   |
| hexiom                   | 10.9 ms                                                               | 12.8 ms: 1.18x slower                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 151 ms: 1.18x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 87.1 ms: 1.18x slower                                                  |
| 2to3                     | 381 ms                                                                | 463 ms: 1.22x slower                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 241 ms: 1.22x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.23x slower                                                  |
| deltablue                | 8.94 ms                                                               | 11.0 ms: 1.23x slower                                                  |
| sympy_expand             | 543 ms                                                                | 674 ms: 1.24x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 455 us: 1.25x slower                                                   |
| html5lib                 | 86.5 ms                                                               | 108 ms: 1.25x slower                                                   |
| django_template          | 53.3 ms                                                               | 66.8 ms: 1.25x slower                                                  |
| sqlalchemy_imperative    | 20.5 ms                                                               | 26.1 ms: 1.27x slower                                                  |
| meteor_contest           | 126 ms                                                                | 160 ms: 1.27x slower                                                   |
| fannkuch                 | 546 ms                                                                | 695 ms: 1.27x slower                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 3.64 ms: 1.28x slower                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 3.10 ms: 1.29x slower                                                  |
| go                       | 264 ms                                                                | 341 ms: 1.29x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.07 ms: 1.30x slower                                                  |
| pickle_pure_python       | 529 us                                                                | 702 us: 1.33x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.01 ms: 1.33x slower                                                  |
| mako                     | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                  |
| async_generators         | 452 ms                                                                | 614 ms: 1.36x slower                                                   |
| telco                    | 8.49 ms                                                               | 12.3 ms: 1.45x slower                                                  |
| mypy2                    | 936 ms                                                                | 1.48 sec: 1.58x slower                                                 |
| coverage                 | 83.6 ms                                                               | 145 ms: 1.74x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 12.5 ms: 1.81x slower                                                  |
| python_startup           | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 61.1 ms: 4.20x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.11x slower                                                           |

Benchmark hidden because not significant (7): scimark_lu, regex_effbot, scimark_fft, richards_super, pycparser, pidigits, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.058x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.55x