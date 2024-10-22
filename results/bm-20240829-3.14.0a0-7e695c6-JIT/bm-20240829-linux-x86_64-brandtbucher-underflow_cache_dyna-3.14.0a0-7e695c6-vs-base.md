# Results vs. base

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 282 ms: 1.02x slower                                                        |
| docutils       | 3.04 sec                                                              | 3.30 sec: 1.09x slower                                                      |
| html5lib       | 63.4 ms                                                               | 76.2 ms: 1.20x slower                                                       |
| tornado_http   | 94.7 ms                                                               | 99.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                      |
| coroutines             | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                       |
| asyncio_tcp            | 499 ms                                                                | 503 ms: 1.01x slower                                                        |
| async_tree_io          | 924 ms                                                                | 936 ms: 1.01x slower                                                        |
| async_tree_none_tg     | 307 ms                                                                | 314 ms: 1.02x slower                                                        |
| async_generators       | 454 ms                                                                | 465 ms: 1.03x slower                                                        |
| async_tree_memoization | 395 ms                                                                | 411 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                               | 79.3 ms: 1.03x faster                                                       |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                        |
| float          | 70.4 ms                                                               | 71.1 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                               | 24.4 ms: 1.02x slower                                                       |
| regex_dna      | 210 ms                                                                | 221 ms: 1.05x slower                                                        |
| regex_effbot   | 3.51 ms                                                               | 3.76 ms: 1.07x slower                                                       |
| regex_compile  | 142 ms                                                                | 154 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 203 us: 1.05x faster                                                        |
| xml_etree_generate   | 77.7 ms                                                               | 77.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.5 ms: 1.01x slower                                                       |
| pickle_pure_python   | 302 us                                                                | 310 us: 1.03x slower                                                        |
| json_loads           | 28.6 us                                                               | 29.5 us: 1.03x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 1.99 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 23.1 ms: 1.11x faster                                                       |
| mako            | 9.79 ms                                                               | 9.74 ms: 1.00x faster                                                       |
| genshi_xml      | 59.0 ms                                                               | 64.0 ms: 1.08x slower                                                       |
| django_template | 35.6 ms                                                               | 38.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text              | 25.7 ms                                                               | 23.1 ms: 1.11x faster                                                       |
| logging_silent           | 103 ns                                                                | 94.7 ns: 1.09x faster                                                       |
| scimark_lu               | 109 ms                                                                | 101 ms: 1.08x faster                                                        |
| unpickle_pure_python     | 213 us                                                                | 203 us: 1.05x faster                                                        |
| deepcopy_memo            | 27.0 us                                                               | 26.1 us: 1.03x faster                                                       |
| nbody                    | 82.0 ms                                                               | 79.3 ms: 1.03x faster                                                       |
| nqueens                  | 85.7 ms                                                               | 83.8 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 4.47 ms                                                               | 4.40 ms: 1.02x faster                                                       |
| scimark_monte_carlo      | 62.5 ms                                                               | 61.7 ms: 1.01x faster                                                       |
| pprint_pformat           | 1.49 sec                                                              | 1.48 sec: 1.01x faster                                                      |
| typing_runtime_protocols | 165 us                                                                | 164 us: 1.01x faster                                                        |
| mdp                      | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                      |
| spectral_norm            | 101 ms                                                                | 101 ms: 1.01x faster                                                        |
| xml_etree_generate       | 77.7 ms                                                               | 77.1 ms: 1.01x faster                                                       |
| json                     | 5.32 ms                                                               | 5.28 ms: 1.01x faster                                                       |
| mako                     | 9.79 ms                                                               | 9.74 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                      |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.14 ms                                                               | 7.17 ms: 1.00x slower                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                        |
| pathlib                  | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                       |
| thrift                   | 789 us                                                                | 795 us: 1.01x slower                                                        |
| coroutines               | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                       |
| pyflate                  | 450 ms                                                                | 454 ms: 1.01x slower                                                        |
| asyncio_tcp              | 499 ms                                                                | 503 ms: 1.01x slower                                                        |
| float                    | 70.4 ms                                                               | 71.1 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 97.7 ms                                                               | 98.5 ms: 1.01x slower                                                       |
| async_tree_io            | 924 ms                                                                | 936 ms: 1.01x slower                                                        |
| go                       | 170 ms                                                                | 173 ms: 1.01x slower                                                        |
| bench_thread_pool        | 817 us                                                                | 830 us: 1.02x slower                                                        |
| create_gc_cycles         | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                       |
| chaos                    | 58.6 ms                                                               | 59.6 ms: 1.02x slower                                                       |
| richards_super           | 45.0 ms                                                               | 45.8 ms: 1.02x slower                                                       |
| coverage                 | 85.6 ms                                                               | 87.4 ms: 1.02x slower                                                       |
| async_tree_none_tg       | 307 ms                                                                | 314 ms: 1.02x slower                                                        |
| raytrace                 | 276 ms                                                                | 282 ms: 1.02x slower                                                        |
| fannkuch                 | 372 ms                                                                | 380 ms: 1.02x slower                                                        |
| hexiom                   | 6.89 ms                                                               | 7.04 ms: 1.02x slower                                                       |
| regex_v8                 | 23.9 ms                                                               | 24.4 ms: 1.02x slower                                                       |
| 2to3                     | 276 ms                                                                | 282 ms: 1.02x slower                                                        |
| async_generators         | 454 ms                                                                | 465 ms: 1.03x slower                                                        |
| pickle_pure_python       | 302 us                                                                | 310 us: 1.03x slower                                                        |
| sqlglot_optimize         | 58.1 ms                                                               | 59.7 ms: 1.03x slower                                                       |
| deltablue                | 3.18 ms                                                               | 3.27 ms: 1.03x slower                                                       |
| generators               | 33.3 ms                                                               | 34.3 ms: 1.03x slower                                                       |
| json_loads               | 28.6 us                                                               | 29.5 us: 1.03x slower                                                       |
| logging_simple           | 5.54 us                                                               | 5.73 us: 1.03x slower                                                       |
| tomli_loads              | 1.92 sec                                                              | 1.99 sec: 1.04x slower                                                      |
| async_tree_memoization   | 395 ms                                                                | 411 ms: 1.04x slower                                                        |
| sympy_integrate          | 22.8 ms                                                               | 23.7 ms: 1.04x slower                                                       |
| logging_format           | 6.04 us                                                               | 6.29 us: 1.04x slower                                                       |
| richards                 | 38.6 ms                                                               | 40.4 ms: 1.05x slower                                                       |
| sympy_expand             | 504 ms                                                                | 528 ms: 1.05x slower                                                        |
| sympy_sum                | 171 ms                                                                | 180 ms: 1.05x slower                                                        |
| tornado_http             | 94.7 ms                                                               | 99.5 ms: 1.05x slower                                                       |
| regex_dna                | 210 ms                                                                | 221 ms: 1.05x slower                                                        |
| gc_traversal             | 3.58 ms                                                               | 3.78 ms: 1.05x slower                                                       |
| sqlglot_normalize        | 113 ms                                                                | 120 ms: 1.06x slower                                                        |
| sqlglot_transpile        | 1.69 ms                                                               | 1.80 ms: 1.07x slower                                                       |
| regex_effbot             | 3.51 ms                                                               | 3.76 ms: 1.07x slower                                                       |
| sympy_str                | 299 ms                                                                | 321 ms: 1.07x slower                                                        |
| genshi_xml               | 59.0 ms                                                               | 64.0 ms: 1.08x slower                                                       |
| regex_compile            | 142 ms                                                                | 154 ms: 1.09x slower                                                        |
| docutils                 | 3.04 sec                                                              | 3.30 sec: 1.09x slower                                                      |
| pylint                   | 372 ms                                                                | 406 ms: 1.09x slower                                                        |
| django_template          | 35.6 ms                                                               | 38.9 ms: 1.09x slower                                                       |
| sqlglot_parse            | 1.34 ms                                                               | 1.53 ms: 1.15x slower                                                       |
| pycparser                | 1.18 sec                                                              | 1.42 sec: 1.20x slower                                                      |
| html5lib                 | 63.4 ms                                                               | 76.2 ms: 1.20x slower                                                       |
| scimark_sor              | 116 ms                                                                | 154 ms: 1.33x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (18): pprint_safe_repr, comprehensions, deepcopy_reduce, xml_etree_parse, json_dumps, asyncio_websockets, bench_mp_pool, scimark_fft, xml_etree_process, bpe_tokeniser, deepcopy, telco, async_tree_cpu_io_mixed, async_tree_none, crypto_pyaes, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x