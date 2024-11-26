# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.020x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 283 ms: 1.01x slower                                                      |
| docutils       | 2.91 sec                                                               | 2.94 sec: 1.01x slower                                                    |
| html5lib       | 65.2 ms                                                                | 66.0 ms: 1.01x slower                                                     |
| tornado_http   | 94.6 ms                                                                | 95.0 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 460 ms                                                                 | 454 ms: 1.01x faster                                                      |
| coroutines       | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                     |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (9): async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.1 ms                                                                | 77.8 ms: 1.02x slower                                                     |
| nbody          | 81.7 ms                                                                | 89.2 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 219 ms: 1.01x slower                                                      |
| regex_v8       | 24.7 ms                                                                | 24.9 ms: 1.01x slower                                                     |
| regex_compile  | 139 ms                                                                 | 141 ms: 1.02x slower                                                      |
| regex_effbot   | 3.77 ms                                                                | 3.86 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 26.6 us                                                                | 26.7 us: 1.00x slower                                                     |
| json_dumps           | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 100 ms                                                                 | 102 ms: 1.01x slower                                                      |
| pickle_pure_python   | 316 us                                                                 | 321 us: 1.02x slower                                                      |
| tomli_loads          | 1.92 sec                                                               | 1.97 sec: 1.03x slower                                                    |
| xml_etree_generate   | 78.4 ms                                                                | 80.7 ms: 1.03x slower                                                     |
| unpickle_pure_python | 216 us                                                                 | 223 us: 1.03x slower                                                      |
| xml_etree_process    | 55.3 ms                                                                | 57.4 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.09 ms: 1.01x slower                                                     |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 26.3 ms                                                                | 25.7 ms: 1.02x faster                                                     |
| genshi_xml      | 61.8 ms                                                                | 60.5 ms: 1.02x faster                                                     |
| django_template | 37.1 ms                                                                | 36.7 ms: 1.01x faster                                                     |
| mako            | 9.87 ms                                                                | 10.5 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text              | 26.3 ms                                                                | 25.7 ms: 1.02x faster                                                     |
| genshi_xml               | 61.8 ms                                                                | 60.5 ms: 1.02x faster                                                     |
| async_generators         | 460 ms                                                                 | 454 ms: 1.01x faster                                                      |
| django_template          | 37.1 ms                                                                | 36.7 ms: 1.01x faster                                                     |
| coroutines               | 23.1 ms                                                                | 22.9 ms: 1.01x faster                                                     |
| coverage                 | 84.4 ms                                                                | 83.7 ms: 1.01x faster                                                     |
| pathlib                  | 16.2 ms                                                                | 16.1 ms: 1.01x faster                                                     |
| json_loads               | 26.6 us                                                                | 26.7 us: 1.00x slower                                                     |
| sympy_sum                | 177 ms                                                                 | 178 ms: 1.00x slower                                                      |
| tornado_http             | 94.6 ms                                                                | 95.0 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.05 ms                                                                | 7.09 ms: 1.01x slower                                                     |
| json_dumps               | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                     |
| python_startup           | 11.8 ms                                                                | 11.8 ms: 1.01x slower                                                     |
| sympy_expand             | 503 ms                                                                 | 507 ms: 1.01x slower                                                      |
| sympy_integrate          | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                     |
| bench_mp_pool            | 83.7 ms                                                                | 84.3 ms: 1.01x slower                                                     |
| regex_dna                | 217 ms                                                                 | 219 ms: 1.01x slower                                                      |
| docutils                 | 2.91 sec                                                               | 2.94 sec: 1.01x slower                                                    |
| regex_v8                 | 24.7 ms                                                                | 24.9 ms: 1.01x slower                                                     |
| html5lib                 | 65.2 ms                                                                | 66.0 ms: 1.01x slower                                                     |
| sqlglot_optimize         | 60.1 ms                                                                | 60.8 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 100 ms                                                                 | 102 ms: 1.01x slower                                                      |
| 2to3                     | 279 ms                                                                 | 283 ms: 1.01x slower                                                      |
| thrift                   | 789 us                                                                 | 801 us: 1.01x slower                                                      |
| sqlglot_parse            | 1.34 ms                                                                | 1.36 ms: 1.02x slower                                                     |
| pickle_pure_python       | 316 us                                                                 | 321 us: 1.02x slower                                                      |
| regex_compile            | 139 ms                                                                 | 141 ms: 1.02x slower                                                      |
| bench_thread_pool        | 877 us                                                                 | 893 us: 1.02x slower                                                      |
| dulwich_log              | 66.4 ms                                                                | 67.7 ms: 1.02x slower                                                     |
| sqlglot_normalize        | 115 ms                                                                 | 118 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 722 ms                                                                 | 738 ms: 1.02x slower                                                      |
| float                    | 76.1 ms                                                                | 77.8 ms: 1.02x slower                                                     |
| regex_effbot             | 3.77 ms                                                                | 3.86 ms: 1.02x slower                                                     |
| deepcopy_reduce          | 2.77 us                                                                | 2.84 us: 1.02x slower                                                     |
| generators               | 35.5 ms                                                                | 36.4 ms: 1.03x slower                                                     |
| pycparser                | 1.15 sec                                                               | 1.18 sec: 1.03x slower                                                    |
| pyflate                  | 445 ms                                                                 | 457 ms: 1.03x slower                                                      |
| mdp                      | 2.57 sec                                                               | 2.64 sec: 1.03x slower                                                    |
| typing_runtime_protocols | 169 us                                                                 | 173 us: 1.03x slower                                                      |
| tomli_loads              | 1.92 sec                                                               | 1.97 sec: 1.03x slower                                                    |
| logging_silent           | 109 ns                                                                 | 112 ns: 1.03x slower                                                      |
| xml_etree_generate       | 78.4 ms                                                                | 80.7 ms: 1.03x slower                                                     |
| scimark_fft              | 323 ms                                                                 | 333 ms: 1.03x slower                                                      |
| deepcopy                 | 269 us                                                                 | 278 us: 1.03x slower                                                      |
| meteor_contest           | 108 ms                                                                 | 112 ms: 1.03x slower                                                      |
| unpickle_pure_python     | 216 us                                                                 | 223 us: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 4.60 ms                                                                | 4.76 ms: 1.03x slower                                                     |
| chaos                    | 59.7 ms                                                                | 61.9 ms: 1.04x slower                                                     |
| xml_etree_process        | 55.3 ms                                                                | 57.4 ms: 1.04x slower                                                     |
| gc_traversal             | 4.55 ms                                                                | 4.74 ms: 1.04x slower                                                     |
| go                       | 133 ms                                                                 | 139 ms: 1.04x slower                                                      |
| raytrace                 | 283 ms                                                                 | 295 ms: 1.04x slower                                                      |
| pprint_pformat           | 1.48 sec                                                               | 1.54 sec: 1.04x slower                                                    |
| bpe_tokeniser            | 4.44 sec                                                               | 4.63 sec: 1.04x slower                                                    |
| spectral_norm            | 116 ms                                                                 | 121 ms: 1.04x slower                                                      |
| hexiom                   | 7.13 ms                                                                | 7.45 ms: 1.05x slower                                                     |
| telco                    | 7.59 ms                                                                | 7.99 ms: 1.05x slower                                                     |
| scimark_monte_carlo      | 64.5 ms                                                                | 67.9 ms: 1.05x slower                                                     |
| nqueens                  | 88.8 ms                                                                | 93.8 ms: 1.06x slower                                                     |
| comprehensions           | 17.0 us                                                                | 18.0 us: 1.06x slower                                                     |
| crypto_pyaes             | 68.3 ms                                                                | 72.6 ms: 1.06x slower                                                     |
| deltablue                | 3.23 ms                                                                | 3.44 ms: 1.06x slower                                                     |
| scimark_sor              | 119 ms                                                                 | 126 ms: 1.06x slower                                                      |
| mako                     | 9.87 ms                                                                | 10.5 ms: 1.07x slower                                                     |
| richards_super           | 45.5 ms                                                                | 48.5 ms: 1.07x slower                                                     |
| richards                 | 41.8 ms                                                                | 44.8 ms: 1.07x slower                                                     |
| deepcopy_memo            | 29.3 us                                                                | 31.8 us: 1.08x slower                                                     |
| nbody                    | 81.7 ms                                                                | 89.2 ms: 1.09x slower                                                     |
| fannkuch                 | 376 ms                                                                 | 411 ms: 1.09x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (22): logging_format, xml_etree_parse, sqlglot_transpile, async_tree_io_tg, sqlalchemy_declarative, asyncio_websockets, scimark_lu, pidigits, create_gc_cycles, async_tree_none_tg, async_tree_io, logging_simple, sympy_str, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pylint, json, sqlalchemy_imperative, async_tree_memoization, sphinx, async_tree_cpu_io_mixed, async_tree_none

- Geometric mean (including insignificant results): 1.020x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x