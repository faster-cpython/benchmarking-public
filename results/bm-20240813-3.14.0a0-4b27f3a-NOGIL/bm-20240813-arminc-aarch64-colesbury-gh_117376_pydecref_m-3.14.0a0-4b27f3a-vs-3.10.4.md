# Results vs. 3.10.4

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-aarch64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 513 ms: 1.35x slower                                                       |
| docutils       | 3.53 sec                                                              | 4.09 sec: 1.16x slower                                                     |
| html5lib       | 86.5 ms                                                               | 120 ms: 1.39x slower                                                       |
| tornado_http   | 178 ms                                                                | 206 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.40 sec: 1.64x faster                                                     |
| async_tree_none         | 950 ms                                                                | 607 ms: 1.56x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 739 ms: 1.53x faster                                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 914 ms: 1.39x faster                                                       |
| Geometric mean          | (ref)                                                                 | 1.53x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 208 ms: 1.54x slower                                                       |
| nbody          | 166 ms                                                                | 281 ms: 1.69x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.38x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 33.4 ms: 1.04x slower                                                      |
| regex_effbot   | 4.25 ms                                                               | 4.51 ms: 1.06x slower                                                      |
| regex_compile  | 177 ms                                                                | 254 ms: 1.44x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 17.8 ms: 1.07x slower                                                      |
| tomli_loads          | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                     |
| json_loads           | 30.9 us                                                               | 39.1 us: 1.26x slower                                                      |
| xml_etree_generate   | 123 ms                                                                | 161 ms: 1.31x slower                                                       |
| xml_etree_process    | 99.5 ms                                                               | 131 ms: 1.32x slower                                                       |
| pickle_pure_python   | 529 us                                                                | 783 us: 1.48x slower                                                       |
| unpickle_pure_python | 366 us                                                                | 541 us: 1.48x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.21x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 17.8 ms: 1.59x slower                                                      |
| python_startup_no_site | 6.89 ms                                                               | 11.9 ms: 1.72x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.66x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.49x slower                                                       |
| mako            | 18.9 ms                                                               | 29.0 ms: 1.53x slower                                                      |
| genshi_text     | 35.2 ms                                                               | 53.9 ms: 1.53x slower                                                      |
| django_template | 53.3 ms                                                               | 82.2 ms: 1.54x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.52x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.91 ms: 2.10x faster                                                      |
| typing_runtime_protocols | 661 us                                                                | 347 us: 1.91x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.40 sec: 1.64x faster                                                     |
| async_tree_none          | 950 ms                                                                | 607 ms: 1.56x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 739 ms: 1.53x faster                                                       |
| asyncio_tcp              | 944 ms                                                                | 661 ms: 1.43x faster                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 1.61 ms: 1.41x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 914 ms: 1.39x faster                                                       |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.43 sec: 1.35x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 3.44 ms: 1.21x faster                                                      |
| generators               | 68.1 ms                                                               | 56.6 ms: 1.20x faster                                                      |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                       |
| crypto_pyaes             | 134 ms                                                                | 136 ms: 1.02x slower                                                       |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                       |
| regex_v8                 | 32.2 ms                                                               | 33.4 ms: 1.04x slower                                                      |
| pylint                   | 485 ms                                                                | 507 ms: 1.04x slower                                                       |
| coroutines               | 37.2 ms                                                               | 39.1 ms: 1.05x slower                                                      |
| regex_effbot             | 4.25 ms                                                               | 4.51 ms: 1.06x slower                                                      |
| json_dumps               | 16.7 ms                                                               | 17.8 ms: 1.07x slower                                                      |
| deepcopy                 | 511 us                                                                | 560 us: 1.10x slower                                                       |
| scimark_fft              | 500 ms                                                                | 572 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.79 ms: 1.15x slower                                                      |
| tornado_http             | 178 ms                                                                | 206 ms: 1.15x slower                                                       |
| docutils                 | 3.53 sec                                                              | 4.09 sec: 1.16x slower                                                     |
| mdp                      | 3.70 sec                                                              | 4.32 sec: 1.17x slower                                                     |
| deepcopy_memo            | 61.7 us                                                               | 72.5 us: 1.18x slower                                                      |
| json                     | 5.88 ms                                                               | 7.09 ms: 1.21x slower                                                      |
| pycparser                | 1.69 sec                                                              | 2.06 sec: 1.22x slower                                                     |
| spectral_norm            | 186 ms                                                                | 227 ms: 1.22x slower                                                       |
| comprehensions           | 33.1 us                                                               | 41.0 us: 1.24x slower                                                      |
| tomli_loads              | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                     |
| logging_silent           | 222 ns                                                                | 279 ns: 1.25x slower                                                       |
| json_loads               | 30.9 us                                                               | 39.1 us: 1.26x slower                                                      |
| richards                 | 91.7 ms                                                               | 116 ms: 1.26x slower                                                       |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                     |
| nqueens                  | 117 ms                                                                | 151 ms: 1.29x slower                                                       |
| chaos                    | 121 ms                                                                | 158 ms: 1.30x slower                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 6.00 us: 1.31x slower                                                      |
| richards_super           | 107 ms                                                                | 140 ms: 1.31x slower                                                       |
| sympy_integrate          | 26.5 ms                                                               | 34.8 ms: 1.31x slower                                                      |
| xml_etree_generate       | 123 ms                                                                | 161 ms: 1.31x slower                                                       |
| xml_etree_process        | 99.5 ms                                                               | 131 ms: 1.32x slower                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 2.11 ms: 1.33x slower                                                      |
| meteor_contest           | 126 ms                                                                | 169 ms: 1.34x slower                                                       |
| 2to3                     | 381 ms                                                                | 513 ms: 1.35x slower                                                       |
| thrift                   | 1.26 ms                                                               | 1.70 ms: 1.35x slower                                                      |
| scimark_monte_carlo      | 128 ms                                                                | 173 ms: 1.35x slower                                                       |
| fannkuch                 | 546 ms                                                                | 738 ms: 1.35x slower                                                       |
| scimark_sor              | 246 ms                                                                | 336 ms: 1.37x slower                                                       |
| html5lib                 | 86.5 ms                                                               | 120 ms: 1.39x slower                                                       |
| raytrace                 | 573 ms                                                                | 803 ms: 1.40x slower                                                       |
| deltablue                | 8.94 ms                                                               | 12.5 ms: 1.40x slower                                                      |
| hexiom                   | 10.9 ms                                                               | 15.6 ms: 1.43x slower                                                      |
| regex_compile            | 177 ms                                                                | 254 ms: 1.44x slower                                                       |
| logging_simple           | 9.78 us                                                               | 14.4 us: 1.47x slower                                                      |
| logging_format           | 10.6 us                                                               | 15.6 us: 1.47x slower                                                      |
| sqlglot_normalize        | 156 ms                                                                | 230 ms: 1.48x slower                                                       |
| async_generators         | 452 ms                                                                | 668 ms: 1.48x slower                                                       |
| pickle_pure_python       | 529 us                                                                | 783 us: 1.48x slower                                                       |
| unpickle_pure_python     | 366 us                                                                | 541 us: 1.48x slower                                                       |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.49x slower                                                       |
| sqlglot_parse            | 2.40 ms                                                               | 3.59 ms: 1.49x slower                                                      |
| telco                    | 8.49 ms                                                               | 12.8 ms: 1.51x slower                                                      |
| sqlglot_transpile        | 2.84 ms                                                               | 4.30 ms: 1.51x slower                                                      |
| pprint_safe_repr         | 1.15 sec                                                              | 1.75 sec: 1.53x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 3.61 sec: 1.53x slower                                                     |
| mako                     | 18.9 ms                                                               | 29.0 ms: 1.53x slower                                                      |
| genshi_text              | 35.2 ms                                                               | 53.9 ms: 1.53x slower                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 116 ms: 1.53x slower                                                       |
| django_template          | 53.3 ms                                                               | 82.2 ms: 1.54x slower                                                      |
| float                    | 135 ms                                                                | 208 ms: 1.54x slower                                                       |
| scimark_lu               | 227 ms                                                                | 353 ms: 1.56x slower                                                       |
| sympy_str                | 329 ms                                                                | 516 ms: 1.57x slower                                                       |
| coverage                 | 83.6 ms                                                               | 132 ms: 1.58x slower                                                       |
| python_startup           | 11.2 ms                                                               | 17.8 ms: 1.59x slower                                                      |
| go                       | 264 ms                                                                | 442 ms: 1.67x slower                                                       |
| nbody                    | 166 ms                                                                | 281 ms: 1.69x slower                                                       |
| sympy_sum                | 184 ms                                                                | 316 ms: 1.72x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 11.9 ms: 1.72x slower                                                      |
| sympy_expand             | 543 ms                                                                | 952 ms: 1.75x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                               |

Benchmark hidden because not significant (4): pidigits, pathlib, regex_dna, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.32x