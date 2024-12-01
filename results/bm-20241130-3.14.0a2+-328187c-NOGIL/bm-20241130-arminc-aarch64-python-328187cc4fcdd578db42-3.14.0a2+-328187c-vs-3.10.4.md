# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.149x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 494 ms: 1.30x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                   |
| html5lib       | 86.5 ms                                                               | 117 ms: 1.35x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                   |
| async_tree_none         | 950 ms                                                                | 618 ms: 1.54x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 759 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 928 ms: 1.37x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.51x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 235 ms                                                                | 232 ms: 1.01x faster                                                     |
| nbody          | 166 ms                                                                | 199 ms: 1.20x slower                                                     |
| float          | 135 ms                                                                | 203 ms: 1.51x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 33.6 ms: 1.05x slower                                                    |
| regex_compile  | 177 ms                                                                | 224 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 19.3 ms: 1.15x slower                                                    |
| tomli_loads          | 3.36 sec                                                              | 3.99 sec: 1.19x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 121 ms: 1.22x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 150 ms: 1.22x slower                                                     |
| json_loads           | 30.9 us                                                               | 37.9 us: 1.23x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 735 us: 1.39x slower                                                     |
| unpickle_pure_python | 366 us                                                                | 518 us: 1.42x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.16x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.7 ms: 1.85x slower                                                    |
| python_startup         | 11.2 ms                                                               | 21.4 ms: 1.92x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.88x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 89.7 ms: 1.28x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 45.8 ms: 1.30x slower                                                    |
| django_template | 53.3 ms                                                               | 73.6 ms: 1.38x slower                                                    |
| mako            | 18.9 ms                                                               | 28.6 ms: 1.51x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.37x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 296 us: 2.23x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                   |
| async_tree_none          | 950 ms                                                                | 618 ms: 1.54x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 759 ms: 1.49x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 928 ms: 1.37x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| generators               | 68.1 ms                                                               | 59.5 ms: 1.14x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 140 ms: 1.11x faster                                                     |
| deepcopy                 | 511 us                                                                | 482 us: 1.06x faster                                                     |
| pidigits                 | 235 ms                                                                | 232 ms: 1.01x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 62.9 us: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 684 ms: 1.04x slower                                                     |
| regex_v8                 | 32.2 ms                                                               | 33.6 ms: 1.05x slower                                                    |
| scimark_fft              | 500 ms                                                                | 533 ms: 1.07x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.26 sec: 1.15x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 19.3 ms: 1.15x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.81 ms: 1.15x slower                                                    |
| json                     | 5.88 ms                                                               | 6.87 ms: 1.17x slower                                                    |
| pycparser                | 1.69 sec                                                              | 2.00 sec: 1.18x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 3.99 sec: 1.19x slower                                                   |
| nbody                    | 166 ms                                                                | 199 ms: 1.20x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 5.53 us: 1.20x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 121 ms: 1.22x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 150 ms: 1.22x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.9 us: 1.23x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.10 ms: 1.23x slower                                                    |
| comprehensions           | 33.1 us                                                               | 41.3 us: 1.25x slower                                                    |
| nqueens                  | 117 ms                                                                | 148 ms: 1.26x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 2.01 ms: 1.26x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 92.8 ms: 1.26x slower                                                    |
| scimark_lu               | 227 ms                                                                | 287 ms: 1.26x slower                                                     |
| regex_compile            | 177 ms                                                                | 224 ms: 1.27x slower                                                     |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                   |
| richards_super           | 107 ms                                                                | 136 ms: 1.27x slower                                                     |
| meteor_contest           | 126 ms                                                                | 161 ms: 1.27x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 89.7 ms: 1.28x slower                                                    |
| scimark_sor              | 246 ms                                                                | 316 ms: 1.28x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 97.1 ms: 1.29x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 202 ms: 1.29x slower                                                     |
| 2to3                     | 381 ms                                                                | 494 ms: 1.30x slower                                                     |
| richards                 | 91.7 ms                                                               | 119 ms: 1.30x slower                                                     |
| chaos                    | 121 ms                                                                | 158 ms: 1.30x slower                                                     |
| genshi_text              | 35.2 ms                                                               | 45.8 ms: 1.30x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.94 ms: 1.30x slower                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 259 ms: 1.31x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 3.10 sec: 1.31x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.51 sec: 1.32x slower                                                   |
| logging_silent           | 222 ns                                                                | 293 ns: 1.32x slower                                                     |
| sympy_integrate          | 26.5 ms                                                               | 35.1 ms: 1.32x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 170 ms: 1.33x slower                                                     |
| thrift                   | 1.26 ms                                                               | 1.70 ms: 1.35x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 14.7 ms: 1.35x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 117 ms: 1.35x slower                                                     |
| fannkuch                 | 546 ms                                                                | 746 ms: 1.37x slower                                                     |
| deltablue                | 8.94 ms                                                               | 12.3 ms: 1.38x slower                                                    |
| django_template          | 53.3 ms                                                               | 73.6 ms: 1.38x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 735 us: 1.39x slower                                                     |
| logging_simple           | 9.78 us                                                               | 13.6 us: 1.39x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 28.6 ms: 1.39x slower                                                    |
| raytrace                 | 573 ms                                                                | 811 ms: 1.41x slower                                                     |
| unpickle_pure_python     | 366 us                                                                | 518 us: 1.42x slower                                                     |
| logging_format           | 10.6 us                                                               | 15.3 us: 1.44x slower                                                    |
| go                       | 264 ms                                                                | 387 ms: 1.46x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.52 ms: 1.47x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.20 ms: 1.48x slower                                                    |
| sympy_str                | 329 ms                                                                | 486 ms: 1.48x slower                                                     |
| async_generators         | 452 ms                                                                | 670 ms: 1.48x slower                                                     |
| float                    | 135 ms                                                                | 203 ms: 1.51x slower                                                     |
| mako                     | 18.9 ms                                                               | 28.6 ms: 1.51x slower                                                    |
| telco                    | 8.49 ms                                                               | 13.0 ms: 1.53x slower                                                    |
| sympy_sum                | 184 ms                                                                | 292 ms: 1.59x slower                                                     |
| sympy_expand             | 543 ms                                                                | 895 ms: 1.65x slower                                                     |
| coverage                 | 83.6 ms                                                               | 145 ms: 1.73x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.7 ms: 1.85x slower                                                    |
| python_startup           | 11.2 ms                                                               | 21.4 ms: 1.92x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 65.5 ms: 4.51x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.22x slower                                                             |

Benchmark hidden because not significant (8): spectral_norm, regex_effbot, crypto_pyaes, pathlib, sqlite_synth, pylint, regex_dna, coroutines
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.149x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.55x