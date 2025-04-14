# Results vs. 3.10.4

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-aarch64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.274x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 316 ms: 1.20x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 939 ms: 2.43x faster                                                     |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 515 ms: 2.20x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 701 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.4 ms: 1.58x faster                                                    |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                                    |
| regex_dna      | 257 ms                                                                | 244 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 274 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 416 us: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 35.1 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| django_template | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 29.2 ms: 1.21x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 221 us: 3.00x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 939 ms: 2.43x faster                                                     |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 515 ms: 2.20x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.22 ms: 2.12x faster                                                    |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                    |
| richards_super           | 107 ms                                                                | 58.2 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 701 ms: 1.81x faster                                                     |
| chaos                    | 121 ms                                                                | 68.6 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                    |
| raytrace                 | 573 ms                                                                | 336 ms: 1.70x faster                                                     |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                     |
| scimark_sor              | 246 ms                                                                | 153 ms: 1.61x faster                                                     |
| logging_silent           | 222 ns                                                                | 140 ns: 1.58x faster                                                     |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                     |
| float                    | 135 ms                                                                | 85.4 ms: 1.58x faster                                                    |
| go                       | 264 ms                                                                | 169 ms: 1.57x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.4 us: 1.57x faster                                                    |
| pylint                   | 485 ms                                                                | 322 ms: 1.51x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                    |
| deepcopy                 | 511 us                                                                | 342 us: 1.49x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.91 ms: 1.49x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 86.3 ms: 1.48x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| pyflate                  | 795 ms                                                                | 572 ms: 1.39x faster                                                     |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 98.2 ms: 1.36x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.26 us: 1.35x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.88 us: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 274 us: 1.33x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 151 ms: 1.30x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.0 ms: 1.29x faster                                                    |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 416 us: 1.27x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.8 ms: 1.22x faster                                                    |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 9.00 ms: 1.21x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 29.2 ms: 1.21x faster                                                    |
| 2to3                     | 381 ms                                                                | 316 ms: 1.20x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                                     |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.43 sec: 1.18x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 133 ms: 1.17x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.9 ms: 1.16x faster                                                    |
| sympy_str                | 329 ms                                                                | 287 ms: 1.14x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 67.6 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.84 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.26 sec: 1.08x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 68.0 ms: 1.08x faster                                                    |
| sympy_expand             | 543 ms                                                                | 504 ms: 1.08x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                     |
| regex_dna                | 257 ms                                                                | 244 ms: 1.06x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.54 sec: 1.05x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.97 us: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| json                     | 5.88 ms                                                               | 6.13 ms: 1.04x slower                                                    |
| async_generators         | 452 ms                                                                | 482 ms: 1.07x slower                                                     |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                                     |
| json_loads               | 30.9 us                                                               | 35.1 us: 1.13x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.78 sec: 1.18x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.35 sec: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.7 ms: 1.19x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.63 ms: 1.61x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.12 ms: 1.71x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.59 sec: 178.39x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                             |

Benchmark hidden because not significant (5): genshi_xml, fannkuch, regex_v8, meteor_contest, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.274x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x