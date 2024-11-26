# Results vs. 3.10.4

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: linux-aarch64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.166x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 402 ms: 1.06x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.78 sec: 1.07x slower                                                   |
| html5lib       | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 624 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 763 ms: 1.67x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.85x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| float          | 135 ms                                                                | 95.6 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 263 ms: 1.02x slower                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 274 us: 1.33x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 412 us: 1.28x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 82.3 ms: 1.21x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.10x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| django_template | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 84.9 ms: 1.22x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 219 us: 3.02x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.30 ms: 2.08x faster                                                    |
| async_tree_none          | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 624 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 763 ms: 1.67x faster                                                     |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                     |
| raytrace                 | 573 ms                                                                | 362 ms: 1.58x faster                                                     |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                     |
| scimark_lu               | 227 ms                                                                | 153 ms: 1.49x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 41.7 us: 1.48x faster                                                    |
| richards_super           | 107 ms                                                                | 73.6 ms: 1.46x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| richards                 | 91.7 ms                                                               | 63.5 ms: 1.44x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 93.1 ms: 1.44x faster                                                    |
| chaos                    | 121 ms                                                                | 84.3 ms: 1.44x faster                                                    |
| float                    | 135 ms                                                                | 95.6 ms: 1.41x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.41x faster                                                    |
| go                       | 264 ms                                                                | 189 ms: 1.40x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 91.9 ms: 1.39x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.4 us: 1.36x faster                                                    |
| generators               | 68.1 ms                                                               | 50.4 ms: 1.35x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 274 us: 1.33x faster                                                     |
| pyflate                  | 795 ms                                                                | 612 ms: 1.30x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.58 us: 1.29x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.20 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 412 us: 1.28x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.30 us: 1.28x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.00 ms: 1.26x faster                                                    |
| deepcopy                 | 511 us                                                                | 407 us: 1.25x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.3 ms: 1.21x faster                                                    |
| spectral_norm            | 186 ms                                                                | 156 ms: 1.19x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 72.9 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.10 us: 1.12x faster                                                    |
| pylint                   | 485 ms                                                                | 433 ms: 1.12x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 15.0 ms: 1.11x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.88 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.10x faster                                                     |
| fannkuch                 | 546 ms                                                                | 500 ms: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                     |
| django_template          | 53.3 ms                                                               | 50.5 ms: 1.06x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 19.6 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.33 ms: 1.04x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.62 sec: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| regex_dna                | 257 ms                                                                | 263 ms: 1.02x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 162 ms: 1.04x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| 2to3                     | 381 ms                                                                | 402 ms: 1.06x slower                                                     |
| nqueens                  | 117 ms                                                                | 124 ms: 1.06x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.78 sec: 1.07x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 28.9 ms: 1.09x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                   |
| sympy_expand             | 543 ms                                                                | 597 ms: 1.10x slower                                                     |
| sympy_str                | 329 ms                                                                | 362 ms: 1.10x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.66 sec: 1.13x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 83.3 ms: 1.13x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 85.5 ms: 1.13x slower                                                    |
| sympy_sum                | 184 ms                                                                | 212 ms: 1.15x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.94 ms: 1.17x slower                                                    |
| async_generators         | 452 ms                                                                | 533 ms: 1.18x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.8 ms: 1.19x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 84.9 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.04 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.30 ms: 1.52x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.84 ms: 1.70x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.58 sec: 109.00x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.08x faster                                                             |

Benchmark hidden because not significant (8): json, genshi_text, sqlalchemy_declarative, meteor_contest, regex_v8, regex_compile, pidigits, sqlite_synth
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.166x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x