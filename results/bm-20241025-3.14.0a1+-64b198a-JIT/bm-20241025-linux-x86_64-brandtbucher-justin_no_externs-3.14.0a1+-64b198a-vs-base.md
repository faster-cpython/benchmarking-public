# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.029x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 286 ms: 1.03x slower                                                      |
| docutils       | 2.91 sec                                                               | 2.97 sec: 1.02x slower                                                    |
| html5lib       | 65.2 ms                                                                | 67.5 ms: 1.03x slower                                                     |
| sphinx         | 1.17 sec                                                               | 1.19 sec: 1.02x slower                                                    |
| tornado_http   | 94.6 ms                                                                | 96.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 460 ms                                                                 | 458 ms: 1.01x faster                                                      |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (10): async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                      |
| float          | 76.1 ms                                                                | 78.6 ms: 1.03x slower                                                     |
| nbody          | 81.7 ms                                                                | 87.6 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 222 ms: 1.02x slower                                                      |
| regex_compile  | 139 ms                                                                 | 142 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 100 ms                                                                 | 102 ms: 1.01x slower                                                      |
| json_loads           | 26.6 us                                                                | 27.1 us: 1.02x slower                                                     |
| pickle_pure_python   | 316 us                                                                 | 326 us: 1.03x slower                                                      |
| json_dumps           | 11.0 ms                                                                | 11.5 ms: 1.04x slower                                                     |
| unpickle_pure_python | 216 us                                                                 | 226 us: 1.05x slower                                                      |
| tomli_loads          | 1.92 sec                                                               | 2.01 sec: 1.05x slower                                                    |
| xml_etree_process    | 55.3 ms                                                                | 58.0 ms: 1.05x slower                                                     |
| xml_etree_generate   | 78.4 ms                                                                | 82.4 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 37.1 ms                                                                | 36.6 ms: 1.01x faster                                                     |
| genshi_text     | 26.3 ms                                                                | 26.5 ms: 1.01x slower                                                     |
| genshi_xml      | 61.8 ms                                                                | 62.9 ms: 1.02x slower                                                     |
| mako            | 9.87 ms                                                                | 10.8 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_format           | 6.22 us                                                                | 6.13 us: 1.01x faster                                                     |
| django_template          | 37.1 ms                                                                | 36.6 ms: 1.01x faster                                                     |
| pathlib                  | 16.2 ms                                                                | 16.1 ms: 1.01x faster                                                     |
| coverage                 | 84.4 ms                                                                | 83.8 ms: 1.01x faster                                                     |
| async_generators         | 460 ms                                                                 | 458 ms: 1.01x faster                                                      |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x faster                                                      |
| create_gc_cycles         | 2.67 ms                                                                | 2.68 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| python_startup           | 11.8 ms                                                                | 11.8 ms: 1.01x slower                                                     |
| sqlglot_transpile        | 1.71 ms                                                                | 1.72 ms: 1.01x slower                                                     |
| sqlalchemy_declarative   | 147 ms                                                                 | 148 ms: 1.01x slower                                                      |
| thrift                   | 789 us                                                                 | 796 us: 1.01x slower                                                      |
| genshi_text              | 26.3 ms                                                                | 26.5 ms: 1.01x slower                                                     |
| pylint                   | 325 ms                                                                 | 329 ms: 1.01x slower                                                      |
| bench_mp_pool            | 83.7 ms                                                                | 84.7 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 100 ms                                                                 | 102 ms: 1.01x slower                                                      |
| sympy_integrate          | 23.6 ms                                                                | 24.0 ms: 1.02x slower                                                     |
| json_loads               | 26.6 us                                                                | 27.1 us: 1.02x slower                                                     |
| genshi_xml               | 61.8 ms                                                                | 62.9 ms: 1.02x slower                                                     |
| bench_thread_pool        | 877 us                                                                 | 893 us: 1.02x slower                                                      |
| sqlglot_parse            | 1.34 ms                                                                | 1.36 ms: 1.02x slower                                                     |
| tornado_http             | 94.6 ms                                                                | 96.4 ms: 1.02x slower                                                     |
| sqlalchemy_imperative    | 17.8 ms                                                                | 18.2 ms: 1.02x slower                                                     |
| docutils                 | 2.91 sec                                                               | 2.97 sec: 1.02x slower                                                    |
| sphinx                   | 1.17 sec                                                               | 1.19 sec: 1.02x slower                                                    |
| sympy_sum                | 177 ms                                                                 | 180 ms: 1.02x slower                                                      |
| sympy_str                | 306 ms                                                                 | 312 ms: 1.02x slower                                                      |
| pycparser                | 1.15 sec                                                               | 1.18 sec: 1.02x slower                                                    |
| regex_dna                | 217 ms                                                                 | 222 ms: 1.02x slower                                                      |
| regex_compile            | 139 ms                                                                 | 142 ms: 1.02x slower                                                      |
| sympy_expand             | 503 ms                                                                 | 516 ms: 1.02x slower                                                      |
| sqlglot_optimize         | 60.1 ms                                                                | 61.6 ms: 1.02x slower                                                     |
| json                     | 4.98 ms                                                                | 5.11 ms: 1.03x slower                                                     |
| 2to3                     | 279 ms                                                                 | 286 ms: 1.03x slower                                                      |
| logging_silent           | 109 ns                                                                 | 111 ns: 1.03x slower                                                      |
| sqlglot_normalize        | 115 ms                                                                 | 118 ms: 1.03x slower                                                      |
| typing_runtime_protocols | 169 us                                                                 | 173 us: 1.03x slower                                                      |
| dulwich_log              | 66.4 ms                                                                | 68.5 ms: 1.03x slower                                                     |
| pickle_pure_python       | 316 us                                                                 | 326 us: 1.03x slower                                                      |
| float                    | 76.1 ms                                                                | 78.6 ms: 1.03x slower                                                     |
| html5lib                 | 65.2 ms                                                                | 67.5 ms: 1.03x slower                                                     |
| json_dumps               | 11.0 ms                                                                | 11.5 ms: 1.04x slower                                                     |
| scimark_fft              | 323 ms                                                                 | 336 ms: 1.04x slower                                                      |
| deepcopy_reduce          | 2.77 us                                                                | 2.88 us: 1.04x slower                                                     |
| gc_traversal             | 4.55 ms                                                                | 4.75 ms: 1.04x slower                                                     |
| meteor_contest           | 108 ms                                                                 | 113 ms: 1.04x slower                                                      |
| unpickle_pure_python     | 216 us                                                                 | 226 us: 1.05x slower                                                      |
| tomli_loads              | 1.92 sec                                                               | 2.01 sec: 1.05x slower                                                    |
| xml_etree_process        | 55.3 ms                                                                | 58.0 ms: 1.05x slower                                                     |
| deepcopy                 | 269 us                                                                 | 283 us: 1.05x slower                                                      |
| raytrace                 | 283 ms                                                                 | 297 ms: 1.05x slower                                                      |
| go                       | 133 ms                                                                 | 140 ms: 1.05x slower                                                      |
| nqueens                  | 88.8 ms                                                                | 93.2 ms: 1.05x slower                                                     |
| xml_etree_generate       | 78.4 ms                                                                | 82.4 ms: 1.05x slower                                                     |
| bpe_tokeniser            | 4.44 sec                                                               | 4.67 sec: 1.05x slower                                                    |
| pprint_pformat           | 1.48 sec                                                               | 1.56 sec: 1.05x slower                                                    |
| chaos                    | 59.7 ms                                                                | 63.2 ms: 1.06x slower                                                     |
| telco                    | 7.59 ms                                                                | 8.04 ms: 1.06x slower                                                     |
| generators               | 35.5 ms                                                                | 37.6 ms: 1.06x slower                                                     |
| spectral_norm            | 116 ms                                                                 | 123 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 722 ms                                                                 | 766 ms: 1.06x slower                                                      |
| deltablue                | 3.23 ms                                                                | 3.44 ms: 1.07x slower                                                     |
| hexiom                   | 7.13 ms                                                                | 7.60 ms: 1.07x slower                                                     |
| deepcopy_memo            | 29.3 us                                                                | 31.3 us: 1.07x slower                                                     |
| crypto_pyaes             | 68.3 ms                                                                | 73.0 ms: 1.07x slower                                                     |
| mdp                      | 2.57 sec                                                               | 2.75 sec: 1.07x slower                                                    |
| scimark_sor              | 119 ms                                                                 | 127 ms: 1.07x slower                                                      |
| nbody                    | 81.7 ms                                                                | 87.6 ms: 1.07x slower                                                     |
| scimark_sparse_mat_mult  | 4.60 ms                                                                | 4.96 ms: 1.08x slower                                                     |
| pyflate                  | 445 ms                                                                 | 480 ms: 1.08x slower                                                      |
| scimark_monte_carlo      | 64.5 ms                                                                | 69.6 ms: 1.08x slower                                                     |
| richards                 | 41.8 ms                                                                | 45.3 ms: 1.08x slower                                                     |
| fannkuch                 | 376 ms                                                                 | 409 ms: 1.09x slower                                                      |
| richards_super           | 45.5 ms                                                                | 49.7 ms: 1.09x slower                                                     |
| mako                     | 9.87 ms                                                                | 10.8 ms: 1.09x slower                                                     |
| comprehensions           | 17.0 us                                                                | 18.8 us: 1.10x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (15): async_tree_io_tg, logging_simple, regex_effbot, xml_etree_parse, regex_v8, asyncio_websockets, scimark_lu, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

- Geometric mean (including insignificant results): 1.029x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x