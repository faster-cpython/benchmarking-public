# Results vs. base

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.002x slower
- HPT reliability: 97.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 276 ms: 1.00x slower                                                   |
| docutils       | 3.03 sec                                                              | 3.01 sec: 1.00x faster                                                 |
| tornado_http   | 95.6 ms                                                               | 97.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                 |
| async_tree_io   | 932 ms                                                                | 938 ms: 1.01x slower                                                   |
| coroutines      | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                  |
| asyncio_tcp     | 485 ms                                                                | 495 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, async_generators, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 24.8 ms                                                               | 24.7 ms: 1.00x faster                                                  |
| regex_compile  | 142 ms                                                                | 142 ms: 1.00x slower                                                   |
| regex_dna      | 219 ms                                                                | 221 ms: 1.01x slower                                                   |
| regex_effbot   | 3.55 ms                                                               | 3.71 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 199 us: 1.09x faster                                                   |
| json_loads           | 28.6 us                                                               | 28.2 us: 1.01x faster                                                  |
| json_dumps           | 10.3 ms                                                               | 10.3 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 98.0 ms                                                               | 98.6 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (5): tomli_loads, pickle_pure_python, xml_etree_generate, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                                  |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                               | 57.3 ms: 1.01x faster                                                  |
| mako            | 9.77 ms                                                               | 9.81 ms: 1.00x slower                                                  |
| genshi_text     | 24.2 ms                                                               | 24.3 ms: 1.01x slower                                                  |
| django_template | 35.6 ms                                                               | 36.2 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent           | 104 ns                                                                | 94.5 ns: 1.10x faster                                                  |
| unpickle_pure_python     | 216 us                                                                | 199 us: 1.09x faster                                                   |
| richards_super           | 45.4 ms                                                               | 42.6 ms: 1.06x faster                                                  |
| deepcopy_memo            | 27.3 us                                                               | 26.0 us: 1.05x faster                                                  |
| json                     | 5.56 ms                                                               | 5.30 ms: 1.05x faster                                                  |
| deepcopy_reduce          | 2.68 us                                                               | 2.64 us: 1.02x faster                                                  |
| genshi_xml               | 58.1 ms                                                               | 57.3 ms: 1.01x faster                                                  |
| json_loads               | 28.6 us                                                               | 28.2 us: 1.01x faster                                                  |
| scimark_sor              | 116 ms                                                                | 115 ms: 1.01x faster                                                   |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                  |
| logging_simple           | 5.70 us                                                               | 5.64 us: 1.01x faster                                                  |
| scimark_lu               | 109 ms                                                                | 109 ms: 1.00x faster                                                   |
| raytrace                 | 274 ms                                                                | 272 ms: 1.00x faster                                                   |
| docutils                 | 3.03 sec                                                              | 3.01 sec: 1.00x faster                                                 |
| sympy_sum                | 173 ms                                                                | 172 ms: 1.00x faster                                                   |
| dulwich_log              | 68.8 ms                                                               | 68.5 ms: 1.00x faster                                                  |
| regex_v8                 | 24.8 ms                                                               | 24.7 ms: 1.00x faster                                                  |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                 |
| 2to3                     | 275 ms                                                                | 276 ms: 1.00x slower                                                   |
| hexiom                   | 6.85 ms                                                               | 6.88 ms: 1.00x slower                                                  |
| mako                     | 9.77 ms                                                               | 9.81 ms: 1.00x slower                                                  |
| regex_compile            | 142 ms                                                                | 142 ms: 1.00x slower                                                   |
| sympy_integrate          | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                                  |
| json_dumps               | 10.3 ms                                                               | 10.3 ms: 1.01x slower                                                  |
| scimark_fft              | 303 ms                                                                | 305 ms: 1.01x slower                                                   |
| genshi_text              | 24.2 ms                                                               | 24.3 ms: 1.01x slower                                                  |
| xml_etree_iterparse      | 98.0 ms                                                               | 98.6 ms: 1.01x slower                                                  |
| sympy_expand             | 504 ms                                                                | 507 ms: 1.01x slower                                                   |
| bench_thread_pool        | 836 us                                                                | 842 us: 1.01x slower                                                   |
| python_startup_no_site   | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                                  |
| async_tree_io            | 932 ms                                                                | 938 ms: 1.01x slower                                                   |
| regex_dna                | 219 ms                                                                | 221 ms: 1.01x slower                                                   |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| create_gc_cycles         | 1.75 ms                                                               | 1.77 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 4.20 ms                                                               | 4.23 ms: 1.01x slower                                                  |
| sqlglot_transpile        | 1.70 ms                                                               | 1.71 ms: 1.01x slower                                                  |
| coroutines               | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                  |
| fannkuch                 | 372 ms                                                                | 376 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 57.7 ms                                                               | 58.3 ms: 1.01x slower                                                  |
| go                       | 130 ms                                                                | 132 ms: 1.01x slower                                                   |
| generators               | 32.9 ms                                                               | 33.3 ms: 1.01x slower                                                  |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| deltablue                | 3.19 ms                                                               | 3.22 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 163 us                                                                | 165 us: 1.01x slower                                                   |
| tornado_http             | 95.6 ms                                                               | 97.0 ms: 1.01x slower                                                  |
| crypto_pyaes             | 65.9 ms                                                               | 66.9 ms: 1.01x slower                                                  |
| django_template          | 35.6 ms                                                               | 36.2 ms: 1.02x slower                                                  |
| chaos                    | 58.7 ms                                                               | 59.7 ms: 1.02x slower                                                  |
| telco                    | 7.82 ms                                                               | 7.97 ms: 1.02x slower                                                  |
| asyncio_tcp              | 485 ms                                                                | 495 ms: 1.02x slower                                                   |
| richards                 | 39.2 ms                                                               | 40.0 ms: 1.02x slower                                                  |
| sqlglot_parse            | 1.34 ms                                                               | 1.37 ms: 1.02x slower                                                  |
| gc_traversal             | 3.56 ms                                                               | 3.66 ms: 1.03x slower                                                  |
| pycparser                | 1.17 sec                                                              | 1.21 sec: 1.03x slower                                                 |
| regex_effbot             | 3.55 ms                                                               | 3.71 ms: 1.05x slower                                                  |
| scimark_monte_carlo      | 62.8 ms                                                               | 67.8 ms: 1.08x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (33): async_tree_none_tg, async_tree_cpu_io_mixed_tg, pprint_pformat, deepcopy, async_tree_cpu_io_mixed, coverage, tomli_loads, logging_format, pyflate, pickle_pure_python, thrift, async_tree_io_tg, sqlglot_normalize, mdp, xml_etree_generate, bpe_tokeniser, asyncio_websockets, sympy_str, pylint, nqueens, async_tree_memoization_tg, async_generators, async_tree_memoization, bench_mp_pool, html5lib, float, async_tree_none, pprint_safe_repr, xml_etree_process, pathlib, nbody, spectral_norm, xml_etree_parse
Ignored benchmarks (7) of results/bm-20240906-3.14.0a0-175d922-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 97.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x