# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 17a27d0
- commit date: 2024-08-08
- overall geometric mean: 1.01x faster
- HPT reliability: 76.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                              | 2.98 sec: 1.02x slower                                                    |
| html5lib       | 63.8 ms                                                               | 65.4 ms: 1.02x slower                                                     |
| tornado_http   | 92.6 ms                                                               | 92.3 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines         | 22.9 ms                                                               | 22.3 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl    | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                    |
| asyncio_websockets | 554 ms                                                                | 558 ms: 1.01x slower                                                      |
| async_tree_none    | 327 ms                                                                | 330 ms: 1.01x slower                                                      |
| asyncio_tcp        | 498 ms                                                                | 504 ms: 1.01x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg, async_generators, async_tree_none_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| float          | 70.5 ms                                                               | 70.9 ms: 1.00x slower                                                     |
| nbody          | 79.1 ms                                                               | 80.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.63 ms: 1.05x faster                                                     |
| regex_v8       | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                                     |
| regex_dna      | 223 ms                                                                | 219 ms: 1.02x faster                                                      |
| regex_compile  | 135 ms                                                                | 137 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 211 us: 1.02x faster                                                      |
| xml_etree_process    | 57.2 ms                                                               | 56.2 ms: 1.02x faster                                                     |
| xml_etree_generate   | 81.6 ms                                                               | 80.3 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                     |
| tomli_loads          | 1.91 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| json_loads           | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.18 ms: 1.00x slower                                                     |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 9.85 ms                                                               | 9.77 ms: 1.01x faster                                                     |
| genshi_xml     | 53.4 ms                                                               | 54.5 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240808-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-17a27d0 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue                | 3.58 ms                                                               | 3.08 ms: 1.16x faster                                                     |
| deepcopy_memo            | 29.1 us                                                               | 26.7 us: 1.09x faster                                                     |
| deepcopy_reduce          | 2.78 us                                                               | 2.63 us: 1.06x faster                                                     |
| gc_traversal             | 3.85 ms                                                               | 3.65 ms: 1.06x faster                                                     |
| regex_effbot             | 3.83 ms                                                               | 3.63 ms: 1.05x faster                                                     |
| logging_silent           | 104 ns                                                                | 99.8 ns: 1.05x faster                                                     |
| richards_super           | 47.5 ms                                                               | 45.5 ms: 1.05x faster                                                     |
| richards                 | 41.2 ms                                                               | 39.6 ms: 1.04x faster                                                     |
| pycparser                | 1.19 sec                                                              | 1.15 sec: 1.04x faster                                                    |
| telco                    | 7.97 ms                                                               | 7.73 ms: 1.03x faster                                                     |
| deepcopy                 | 273 us                                                                | 266 us: 1.03x faster                                                      |
| coroutines               | 22.9 ms                                                               | 22.3 ms: 1.03x faster                                                     |
| unpickle_pure_python     | 215 us                                                                | 211 us: 1.02x faster                                                      |
| regex_v8                 | 24.4 ms                                                               | 23.9 ms: 1.02x faster                                                     |
| xml_etree_process        | 57.2 ms                                                               | 56.2 ms: 1.02x faster                                                     |
| chaos                    | 58.1 ms                                                               | 57.1 ms: 1.02x faster                                                     |
| regex_dna                | 223 ms                                                                | 219 ms: 1.02x faster                                                      |
| xml_etree_generate       | 81.6 ms                                                               | 80.3 ms: 1.02x faster                                                     |
| raytrace                 | 269 ms                                                                | 265 ms: 1.02x faster                                                      |
| sympy_expand             | 508 ms                                                                | 501 ms: 1.01x faster                                                      |
| scimark_sor              | 117 ms                                                                | 115 ms: 1.01x faster                                                      |
| go                       | 146 ms                                                                | 144 ms: 1.01x faster                                                      |
| scimark_lu               | 109 ms                                                                | 107 ms: 1.01x faster                                                      |
| fannkuch                 | 371 ms                                                                | 366 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.01x faster                                                      |
| logging_simple           | 5.57 us                                                               | 5.51 us: 1.01x faster                                                     |
| logging_format           | 6.17 us                                                               | 6.11 us: 1.01x faster                                                     |
| mdp                      | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                    |
| mako                     | 9.85 ms                                                               | 9.77 ms: 1.01x faster                                                     |
| create_gc_cycles         | 1.78 ms                                                               | 1.77 ms: 1.01x faster                                                     |
| xml_etree_iterparse      | 99.2 ms                                                               | 98.5 ms: 1.01x faster                                                     |
| tomli_loads              | 1.91 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.01x faster                                                      |
| thrift                   | 797 us                                                                | 793 us: 1.01x faster                                                      |
| sympy_str                | 298 ms                                                                | 297 ms: 1.00x faster                                                      |
| bench_thread_pool        | 822 us                                                                | 819 us: 1.00x faster                                                      |
| tornado_http             | 92.6 ms                                                               | 92.3 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                    |
| python_startup_no_site   | 7.17 ms                                                               | 7.18 ms: 1.00x slower                                                     |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                     |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| float                    | 70.5 ms                                                               | 70.9 ms: 1.00x slower                                                     |
| asyncio_websockets       | 554 ms                                                                | 558 ms: 1.01x slower                                                      |
| sympy_sum                | 170 ms                                                                | 172 ms: 1.01x slower                                                      |
| sqlglot_transpile        | 1.62 ms                                                               | 1.64 ms: 1.01x slower                                                     |
| json_loads               | 27.7 us                                                               | 28.0 us: 1.01x slower                                                     |
| async_tree_none          | 327 ms                                                                | 330 ms: 1.01x slower                                                      |
| pyflate                  | 432 ms                                                                | 436 ms: 1.01x slower                                                      |
| asyncio_tcp              | 498 ms                                                                | 504 ms: 1.01x slower                                                      |
| nbody                    | 79.1 ms                                                               | 80.1 ms: 1.01x slower                                                     |
| regex_compile            | 135 ms                                                                | 137 ms: 1.02x slower                                                      |
| scimark_fft              | 307 ms                                                                | 312 ms: 1.02x slower                                                      |
| comprehensions           | 16.2 us                                                               | 16.5 us: 1.02x slower                                                     |
| genshi_xml               | 53.4 ms                                                               | 54.5 ms: 1.02x slower                                                     |
| docutils                 | 2.92 sec                                                              | 2.98 sec: 1.02x slower                                                    |
| pprint_safe_repr         | 722 ms                                                                | 737 ms: 1.02x slower                                                      |
| sqlglot_optimize         | 55.9 ms                                                               | 57.0 ms: 1.02x slower                                                     |
| pprint_pformat           | 1.49 sec                                                              | 1.52 sec: 1.02x slower                                                    |
| html5lib                 | 63.8 ms                                                               | 65.4 ms: 1.02x slower                                                     |
| scimark_monte_carlo      | 60.7 ms                                                               | 62.3 ms: 1.03x slower                                                     |
| spectral_norm            | 100 ms                                                                | 105 ms: 1.05x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed_tg, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, json_dumps, django_template, async_tree_io, async_tree_memoization_tg, json, pickle_pure_python, coverage, generators, 2to3, crypto_pyaes, nqueens, meteor_contest, bench_mp_pool, sqlglot_parse, async_generators, bpe_tokeniser, genshi_text, sympy_integrate, pathlib, async_tree_none_tg, hexiom, async_tree_io_tg, xml_etree_parse, async_tree_memoization, pylint

# HPT report

- Reliability score: 76.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x