# Results vs. base

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 254 ms: 1.00x slower                                                     |
| docutils       | 2.70 sec                                                              | 2.69 sec: 1.01x faster                                                   |
| html5lib       | 66.3 ms                                                               | 64.9 ms: 1.02x faster                                                    |
| tornado_http   | 90.5 ms                                                               | 90.2 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                               | 23.2 ms: 1.01x faster                                                    |
| asyncio_tcp      | 483 ms                                                                | 479 ms: 1.01x faster                                                     |
| async_generators | 434 ms                                                                | 431 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                   |
| Geometric mean   | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.9 ms                                                               | 76.9 ms: 1.01x faster                                                    |
| nbody          | 87.1 ms                                                               | 86.0 ms: 1.01x faster                                                    |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.74 ms                                                               | 3.48 ms: 1.07x faster                                                    |
| regex_dna      | 225 ms                                                                | 219 ms: 1.03x faster                                                     |
| regex_compile  | 128 ms                                                                | 126 ms: 1.01x faster                                                     |
| regex_v8       | 23.9 ms                                                               | 25.0 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 211 us: 1.02x faster                                                     |
| pickle_pure_python   | 300 us                                                                | 298 us: 1.01x faster                                                     |
| xml_etree_process    | 58.6 ms                                                               | 58.3 ms: 1.00x faster                                                    |
| json_loads           | 28.3 us                                                               | 28.6 us: 1.01x slower                                                    |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                    |
| tomli_loads          | 2.04 sec                                                              | 2.07 sec: 1.01x slower                                                   |
| xml_etree_parse      | 154 ms                                                                | 157 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 21.8 ms                                                               | 21.5 ms: 1.01x faster                                                    |
| mako           | 11.2 ms                                                               | 11.4 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-linux-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| logging_silent           | 103 ns                                                                | 94.5 ns: 1.09x faster                                                    |
| regex_effbot             | 3.74 ms                                                               | 3.48 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult  | 4.79 ms                                                               | 4.55 ms: 1.05x faster                                                    |
| scimark_fft              | 371 ms                                                                | 359 ms: 1.03x faster                                                     |
| deepcopy_memo            | 29.9 us                                                               | 29.0 us: 1.03x faster                                                    |
| pyflate                  | 468 ms                                                                | 454 ms: 1.03x faster                                                     |
| regex_dna                | 225 ms                                                                | 219 ms: 1.03x faster                                                     |
| scimark_lu               | 115 ms                                                                | 113 ms: 1.02x faster                                                     |
| scimark_sor              | 126 ms                                                                | 123 ms: 1.02x faster                                                     |
| html5lib                 | 66.3 ms                                                               | 64.9 ms: 1.02x faster                                                    |
| unpickle_pure_python     | 215 us                                                                | 211 us: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                                | 106 ms: 1.02x faster                                                     |
| go                       | 162 ms                                                                | 159 ms: 1.02x faster                                                     |
| pprint_pformat           | 1.48 sec                                                              | 1.46 sec: 1.02x faster                                                   |
| mdp                      | 2.69 sec                                                              | 2.65 sec: 1.02x faster                                                   |
| spectral_norm            | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| sqlglot_optimize         | 53.8 ms                                                               | 53.1 ms: 1.01x faster                                                    |
| pprint_safe_repr         | 723 ms                                                                | 714 ms: 1.01x faster                                                     |
| genshi_text              | 21.8 ms                                                               | 21.5 ms: 1.01x faster                                                    |
| regex_compile            | 128 ms                                                                | 126 ms: 1.01x faster                                                     |
| float                    | 77.9 ms                                                               | 76.9 ms: 1.01x faster                                                    |
| chaos                    | 58.7 ms                                                               | 58.0 ms: 1.01x faster                                                    |
| nbody                    | 87.1 ms                                                               | 86.0 ms: 1.01x faster                                                    |
| fannkuch                 | 403 ms                                                                | 399 ms: 1.01x faster                                                     |
| coroutines               | 23.4 ms                                                               | 23.2 ms: 1.01x faster                                                    |
| raytrace                 | 262 ms                                                                | 259 ms: 1.01x faster                                                     |
| sympy_str                | 269 ms                                                                | 267 ms: 1.01x faster                                                     |
| crypto_pyaes             | 73.1 ms                                                               | 72.4 ms: 1.01x faster                                                    |
| sympy_integrate          | 19.6 ms                                                               | 19.4 ms: 1.01x faster                                                    |
| asyncio_tcp              | 483 ms                                                                | 479 ms: 1.01x faster                                                     |
| sympy_expand             | 458 ms                                                                | 455 ms: 1.01x faster                                                     |
| async_generators         | 434 ms                                                                | 431 ms: 1.01x faster                                                     |
| sqlglot_parse            | 1.28 ms                                                               | 1.27 ms: 1.01x faster                                                    |
| sqlglot_transpile        | 1.57 ms                                                               | 1.56 ms: 1.01x faster                                                    |
| hexiom                   | 6.16 ms                                                               | 6.12 ms: 1.01x faster                                                    |
| pickle_pure_python       | 300 us                                                                | 298 us: 1.01x faster                                                     |
| gc_traversal             | 3.74 ms                                                               | 3.72 ms: 1.01x faster                                                    |
| coverage                 | 85.8 ms                                                               | 85.3 ms: 1.01x faster                                                    |
| pathlib                  | 15.9 ms                                                               | 15.9 ms: 1.01x faster                                                    |
| docutils                 | 2.70 sec                                                              | 2.69 sec: 1.01x faster                                                   |
| richards                 | 46.0 ms                                                               | 45.8 ms: 1.00x faster                                                    |
| xml_etree_process        | 58.6 ms                                                               | 58.3 ms: 1.00x faster                                                    |
| bench_thread_pool        | 784 us                                                                | 780 us: 1.00x faster                                                     |
| richards_super           | 51.9 ms                                                               | 51.7 ms: 1.00x faster                                                    |
| deltablue                | 3.19 ms                                                               | 3.17 ms: 1.00x faster                                                    |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                    |
| tornado_http             | 90.5 ms                                                               | 90.2 ms: 1.00x faster                                                    |
| python_startup_no_site   | 7.07 ms                                                               | 7.05 ms: 1.00x faster                                                    |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                   |
| 2to3                     | 254 ms                                                                | 254 ms: 1.00x slower                                                     |
| deepcopy                 | 260 us                                                                | 261 us: 1.01x slower                                                     |
| json_loads               | 28.3 us                                                               | 28.6 us: 1.01x slower                                                    |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                    |
| mako                     | 11.2 ms                                                               | 11.4 ms: 1.01x slower                                                    |
| logging_simple           | 5.55 us                                                               | 5.62 us: 1.01x slower                                                    |
| tomli_loads              | 2.04 sec                                                              | 2.07 sec: 1.01x slower                                                   |
| typing_runtime_protocols | 157 us                                                                | 159 us: 1.02x slower                                                     |
| logging_format           | 6.10 us                                                               | 6.22 us: 1.02x slower                                                    |
| xml_etree_parse          | 154 ms                                                                | 157 ms: 1.02x slower                                                     |
| deepcopy_reduce          | 2.64 us                                                               | 2.72 us: 1.03x slower                                                    |
| regex_v8                 | 23.9 ms                                                               | 25.0 ms: 1.05x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (27): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, pylint, telco, json, async_tree_cpu_io_mixed_tg, sympy_sum, django_template, genshi_xml, xml_etree_generate, create_gc_cycles, asyncio_websockets, pycparser, async_tree_io, bench_mp_pool, thrift, xml_etree_iterparse, meteor_contest, generators, nqueens, comprehensions, bpe_tokeniser, async_tree_io_tg, scimark_monte_carlo

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x