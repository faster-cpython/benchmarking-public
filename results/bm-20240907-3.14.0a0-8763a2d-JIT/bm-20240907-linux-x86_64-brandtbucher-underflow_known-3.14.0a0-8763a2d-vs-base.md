# Results vs. base

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.01x slower
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 281 ms: 1.02x slower                                                   |
| docutils       | 3.03 sec                                                              | 3.01 sec: 1.01x faster                                                 |
| html5lib       | 64.7 ms                                                               | 61.9 ms: 1.05x faster                                                  |
| tornado_http   | 95.6 ms                                                               | 96.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 571 ms                                                                | 563 ms: 1.01x faster                                                   |
| asyncio_tcp             | 485 ms                                                                | 482 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                 |
| async_generators        | 460 ms                                                                | 462 ms: 1.00x slower                                                   |
| async_tree_io           | 932 ms                                                                | 936 ms: 1.00x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, coroutines, async_tree_io_tg, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                   |
| nbody          | 79.1 ms                                                               | 80.4 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 213 ms: 1.03x faster                                                   |
| regex_v8       | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                  |
| regex_effbot   | 3.55 ms                                                               | 3.62 ms: 1.02x slower                                                  |
| regex_compile  | 142 ms                                                                | 146 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 198 us: 1.10x faster                                                   |
| xml_etree_process    | 55.2 ms                                                               | 54.4 ms: 1.02x faster                                                  |
| xml_etree_generate   | 77.8 ms                                                               | 76.9 ms: 1.01x faster                                                  |
| json_loads           | 28.6 us                                                               | 28.2 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 98.0 ms                                                               | 98.4 ms: 1.00x slower                                                  |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                  |
| tomli_loads          | 1.93 sec                                                              | 1.96 sec: 1.02x slower                                                 |
| pickle_pure_python   | 301 us                                                                | 323 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                  |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                               | 54.1 ms: 1.07x faster                                                  |
| genshi_text    | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                  |
| mako           | 9.77 ms                                                               | 9.72 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python     | 216 us                                                                | 198 us: 1.10x faster                                                   |
| deepcopy_memo            | 27.3 us                                                               | 25.2 us: 1.09x faster                                                  |
| genshi_xml               | 58.1 ms                                                               | 54.1 ms: 1.07x faster                                                  |
| richards_super           | 45.4 ms                                                               | 42.3 ms: 1.07x faster                                                  |
| html5lib                 | 64.7 ms                                                               | 61.9 ms: 1.05x faster                                                  |
| richards                 | 39.2 ms                                                               | 37.8 ms: 1.04x faster                                                  |
| json                     | 5.56 ms                                                               | 5.38 ms: 1.03x faster                                                  |
| logging_silent           | 104 ns                                                                | 101 ns: 1.03x faster                                                   |
| regex_dna                | 219 ms                                                                | 213 ms: 1.03x faster                                                   |
| deltablue                | 3.19 ms                                                               | 3.12 ms: 1.02x faster                                                  |
| xml_etree_process        | 55.2 ms                                                               | 54.4 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed  | 571 ms                                                                | 563 ms: 1.01x faster                                                   |
| regex_v8                 | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                  |
| coverage                 | 86.5 ms                                                               | 85.4 ms: 1.01x faster                                                  |
| xml_etree_generate       | 77.8 ms                                                               | 76.9 ms: 1.01x faster                                                  |
| thrift                   | 781 us                                                                | 771 us: 1.01x faster                                                   |
| json_loads               | 28.6 us                                                               | 28.2 us: 1.01x faster                                                  |
| pathlib                  | 15.9 ms                                                               | 15.7 ms: 1.01x faster                                                  |
| genshi_text              | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                  |
| docutils                 | 3.03 sec                                                              | 3.01 sec: 1.01x faster                                                 |
| asyncio_tcp              | 485 ms                                                                | 482 ms: 1.01x faster                                                   |
| comprehensions           | 16.7 us                                                               | 16.6 us: 1.01x faster                                                  |
| mako                     | 9.77 ms                                                               | 9.72 ms: 1.00x faster                                                  |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                 |
| xml_etree_iterparse      | 98.0 ms                                                               | 98.4 ms: 1.00x slower                                                  |
| async_generators         | 460 ms                                                                | 462 ms: 1.00x slower                                                   |
| async_tree_io            | 932 ms                                                                | 936 ms: 1.00x slower                                                   |
| generators               | 32.9 ms                                                               | 33.1 ms: 1.01x slower                                                  |
| sqlglot_normalize        | 113 ms                                                                | 113 ms: 1.01x slower                                                   |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                  |
| sympy_expand             | 504 ms                                                                | 508 ms: 1.01x slower                                                   |
| pyflate                  | 452 ms                                                                | 455 ms: 1.01x slower                                                   |
| scimark_lu               | 109 ms                                                                | 110 ms: 1.01x slower                                                   |
| gc_traversal             | 3.56 ms                                                               | 3.59 ms: 1.01x slower                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                  |
| crypto_pyaes             | 65.9 ms                                                               | 66.5 ms: 1.01x slower                                                  |
| nqueens                  | 85.2 ms                                                               | 86.2 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 163 us                                                                | 165 us: 1.01x slower                                                   |
| bpe_tokeniser            | 4.43 sec                                                              | 4.48 sec: 1.01x slower                                                 |
| tornado_http             | 95.6 ms                                                               | 96.8 ms: 1.01x slower                                                  |
| sympy_integrate          | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                                  |
| python_startup           | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                  |
| nbody                    | 79.1 ms                                                               | 80.4 ms: 1.02x slower                                                  |
| tomli_loads              | 1.93 sec                                                              | 1.96 sec: 1.02x slower                                                 |
| sqlglot_optimize         | 57.7 ms                                                               | 58.7 ms: 1.02x slower                                                  |
| pprint_pformat           | 1.52 sec                                                              | 1.55 sec: 1.02x slower                                                 |
| telco                    | 7.82 ms                                                               | 7.97 ms: 1.02x slower                                                  |
| spectral_norm            | 99.2 ms                                                               | 101 ms: 1.02x slower                                                   |
| regex_effbot             | 3.55 ms                                                               | 3.62 ms: 1.02x slower                                                  |
| 2to3                     | 275 ms                                                                | 281 ms: 1.02x slower                                                   |
| sympy_str                | 299 ms                                                                | 306 ms: 1.02x slower                                                   |
| sqlglot_parse            | 1.34 ms                                                               | 1.38 ms: 1.03x slower                                                  |
| meteor_contest           | 106 ms                                                                | 109 ms: 1.03x slower                                                   |
| dulwich_log              | 68.8 ms                                                               | 70.8 ms: 1.03x slower                                                  |
| regex_compile            | 142 ms                                                                | 146 ms: 1.03x slower                                                   |
| sympy_sum                | 173 ms                                                                | 179 ms: 1.03x slower                                                   |
| raytrace                 | 274 ms                                                                | 283 ms: 1.03x slower                                                   |
| pprint_safe_repr         | 724 ms                                                                | 751 ms: 1.04x slower                                                   |
| scimark_fft              | 303 ms                                                                | 316 ms: 1.04x slower                                                   |
| chaos                    | 58.7 ms                                                               | 61.6 ms: 1.05x slower                                                  |
| pycparser                | 1.17 sec                                                              | 1.24 sec: 1.05x slower                                                 |
| go                       | 130 ms                                                                | 139 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult  | 4.20 ms                                                               | 4.49 ms: 1.07x slower                                                  |
| pickle_pure_python       | 301 us                                                                | 323 us: 1.07x slower                                                   |
| hexiom                   | 6.85 ms                                                               | 7.72 ms: 1.13x slower                                                  |
| scimark_monte_carlo      | 62.8 ms                                                               | 77.3 ms: 1.23x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (23): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, logging_simple, coroutines, async_tree_io_tg, float, bench_thread_pool, bench_mp_pool, asyncio_websockets, create_gc_cycles, logging_format, fannkuch, deepcopy_reduce, scimark_sor, django_template, async_tree_none, mdp, pylint, deepcopy, xml_etree_parse, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20240907-3.14.0a0-8763a2d-JIT/bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x