# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: e1a3f48
- commit date: 2025-06-29
- overall geometric mean: 1.004x faster
- HPT reliability: 58.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 258 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg | 252 ms                                                                | 248 ms: 1.01x faster                                                |
| coroutines         | 25.3 ms                                                               | 25.1 ms: 1.01x faster                                               |
| async_generators   | 426 ms                                                                | 432 ms: 1.01x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (8): async_tree_memoization_tg, asyncio_websockets, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                                |
| float          | 65.6 ms                                                               | 66.0 ms: 1.01x slower                                               |
| nbody          | 94.8 ms                                                               | 96.1 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                | 200 ms: 1.10x faster                                                |
| regex_v8       | 24.4 ms                                                               | 22.3 ms: 1.09x faster                                               |
| regex_effbot   | 3.43 ms                                                               | 3.23 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                                | 190 us: 1.02x faster                                                |
| json_loads           | 28.7 us                                                               | 28.4 us: 1.01x faster                                               |
| tomli_loads          | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                              |
| xml_etree_parse      | 141 ms                                                                | 140 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.5 ms: 1.00x faster                                               |
| pickle_pure_python   | 320 us                                                                | 324 us: 1.01x slower                                                |
| xml_etree_generate   | 80.0 ms                                                               | 81.2 ms: 1.01x slower                                               |
| xml_etree_process    | 55.5 ms                                                               | 56.6 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                               |
| python_startup         | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                               | 21.8 ms: 1.03x faster                                               |
| django_template | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250629-linux-x86_64-python-39478479146f1f418811-3.15.0a0-3947847 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna                | 220 ms                                                                | 200 ms: 1.10x faster                                                |
| regex_v8                 | 24.4 ms                                                               | 22.3 ms: 1.09x faster                                               |
| gc_traversal             | 5.17 ms                                                               | 4.78 ms: 1.08x faster                                               |
| regex_effbot             | 3.43 ms                                                               | 3.23 ms: 1.06x faster                                               |
| crypto_pyaes             | 74.9 ms                                                               | 71.7 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult  | 5.05 ms                                                               | 4.88 ms: 1.03x faster                                               |
| logging_format           | 6.44 us                                                               | 6.26 us: 1.03x faster                                               |
| nqueens                  | 84.3 ms                                                               | 82.1 ms: 1.03x faster                                               |
| genshi_text              | 22.4 ms                                                               | 21.8 ms: 1.03x faster                                               |
| typing_runtime_protocols | 171 us                                                                | 167 us: 1.02x faster                                                |
| pprint_pformat           | 1.48 sec                                                              | 1.45 sec: 1.02x faster                                              |
| logging_simple           | 5.73 us                                                               | 5.62 us: 1.02x faster                                               |
| pprint_safe_repr         | 721 ms                                                                | 708 ms: 1.02x faster                                                |
| unpickle_pure_python     | 194 us                                                                | 190 us: 1.02x faster                                                |
| go                       | 117 ms                                                                | 115 ms: 1.01x faster                                                |
| json                     | 5.30 ms                                                               | 5.23 ms: 1.01x faster                                               |
| async_tree_none_tg       | 252 ms                                                                | 248 ms: 1.01x faster                                                |
| pathlib                  | 17.1 ms                                                               | 16.9 ms: 1.01x faster                                               |
| json_loads               | 28.7 us                                                               | 28.4 us: 1.01x faster                                               |
| mdp                      | 1.24 sec                                                              | 1.22 sec: 1.01x faster                                              |
| tomli_loads              | 1.83 sec                                                              | 1.81 sec: 1.01x faster                                              |
| raytrace                 | 273 ms                                                                | 270 ms: 1.01x faster                                                |
| deepcopy_memo            | 29.8 us                                                               | 29.4 us: 1.01x faster                                               |
| hexiom                   | 6.27 ms                                                               | 6.21 ms: 1.01x faster                                               |
| scimark_fft              | 315 ms                                                                | 312 ms: 1.01x faster                                                |
| sqlglot_v2_optimize      | 53.1 ms                                                               | 52.7 ms: 1.01x faster                                               |
| python_startup_no_site   | 6.99 ms                                                               | 6.94 ms: 1.01x faster                                               |
| python_startup           | 12.3 ms                                                               | 12.2 ms: 1.01x faster                                               |
| coroutines               | 25.3 ms                                                               | 25.1 ms: 1.01x faster                                               |
| xml_etree_parse          | 141 ms                                                                | 140 ms: 1.01x faster                                                |
| chaos                    | 61.4 ms                                                               | 61.0 ms: 1.01x faster                                               |
| create_gc_cycles         | 2.60 ms                                                               | 2.59 ms: 1.01x faster                                               |
| xml_etree_iterparse      | 99.0 ms                                                               | 98.5 ms: 1.00x faster                                               |
| sqlglot_v2_transpile     | 1.56 ms                                                               | 1.56 ms: 1.00x faster                                               |
| 2to3                     | 259 ms                                                                | 258 ms: 1.00x faster                                                |
| sympy_expand             | 467 ms                                                                | 466 ms: 1.00x faster                                                |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x faster                                                |
| sympy_sum                | 150 ms                                                                | 151 ms: 1.00x slower                                                |
| scimark_sor              | 117 ms                                                                | 117 ms: 1.00x slower                                                |
| sympy_integrate          | 19.4 ms                                                               | 19.4 ms: 1.00x slower                                               |
| sympy_str                | 272 ms                                                                | 273 ms: 1.00x slower                                                |
| float                    | 65.6 ms                                                               | 66.0 ms: 1.01x slower                                               |
| many_optionals           | 975 us                                                                | 981 us: 1.01x slower                                                |
| deepcopy                 | 257 us                                                                | 259 us: 1.01x slower                                                |
| django_template          | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                               |
| telco                    | 7.74 ms                                                               | 7.82 ms: 1.01x slower                                               |
| shortest_path            | 492 ms                                                                | 498 ms: 1.01x slower                                                |
| async_generators         | 426 ms                                                                | 432 ms: 1.01x slower                                                |
| pickle_pure_python       | 320 us                                                                | 324 us: 1.01x slower                                                |
| dulwich_log              | 59.0 ms                                                               | 59.9 ms: 1.01x slower                                               |
| nbody                    | 94.8 ms                                                               | 96.1 ms: 1.01x slower                                               |
| xml_etree_generate       | 80.0 ms                                                               | 81.2 ms: 1.01x slower                                               |
| subparsers               | 23.5 ms                                                               | 23.8 ms: 1.02x slower                                               |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.02x slower                                                |
| connected_components     | 455 ms                                                                | 463 ms: 1.02x slower                                                |
| xml_etree_process        | 55.5 ms                                                               | 56.6 ms: 1.02x slower                                               |
| spectral_norm            | 89.8 ms                                                               | 91.7 ms: 1.02x slower                                               |
| scimark_lu               | 117 ms                                                                | 119 ms: 1.02x slower                                                |
| pyflate                  | 410 ms                                                                | 420 ms: 1.03x slower                                                |
| deepcopy_reduce          | 2.67 us                                                               | 2.75 us: 1.03x slower                                               |
| generators               | 30.0 ms                                                               | 31.3 ms: 1.04x slower                                               |
| richards_super           | 38.1 ms                                                               | 39.8 ms: 1.05x slower                                               |
| richards                 | 32.0 ms                                                               | 34.7 ms: 1.08x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (30): async_tree_memoization_tg, djangocms, sqlglot_v2_normalize, k_core, sphinx, asyncio_websockets, scimark_monte_carlo, sqlglot_v2_parse, thrift, async_tree_memoization, deltablue, pycparser, docutils, regex_compile, mako, async_tree_none, bpe_tokeniser, logging_silent, json_dumps, sqlite_synth, coverage, async_tree_cpu_io_mixed_tg, comprehensions, fannkuch, genshi_xml, async_tree_cpu_io_mixed, pylint, async_tree_io, async_tree_io_tg, html5lib

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 58.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x