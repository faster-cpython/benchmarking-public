# Results vs. base

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 288 ms: 1.04x slower                                                        |
| docutils       | 3.03 sec                                                              | 3.23 sec: 1.07x slower                                                      |
| html5lib       | 64.7 ms                                                               | 67.7 ms: 1.05x slower                                                       |
| tornado_http   | 95.6 ms                                                               | 104 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 571 ms                                                                | 561 ms: 1.02x faster                                                        |
| async_generators        | 460 ms                                                                | 452 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| async_tree_io           | 932 ms                                                                | 938 ms: 1.01x slower                                                        |
| async_tree_memoization  | 401 ms                                                                | 416 ms: 1.04x slower                                                        |
| asyncio_tcp             | 485 ms                                                                | 506 ms: 1.04x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, coroutines, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.2 ms                                                               | 71.4 ms: 1.02x slower                                                       |
| nbody          | 79.1 ms                                                               | 80.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 212 ms: 1.04x faster                                                        |
| regex_effbot   | 3.55 ms                                                               | 3.59 ms: 1.01x slower                                                       |
| regex_v8       | 24.8 ms                                                               | 25.3 ms: 1.02x slower                                                       |
| regex_compile  | 142 ms                                                                | 154 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 201 us: 1.08x faster                                                        |
| xml_etree_process    | 55.2 ms                                                               | 53.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 77.8 ms                                                               | 77.2 ms: 1.01x faster                                                       |
| json_loads           | 28.6 us                                                               | 28.9 us: 1.01x slower                                                       |
| tomli_loads          | 1.93 sec                                                              | 2.07 sec: 1.07x slower                                                      |
| pickle_pure_python   | 301 us                                                                | 330 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 24.2 ms                                                               | 22.8 ms: 1.06x faster                                                       |
| genshi_xml      | 58.1 ms                                                               | 58.7 ms: 1.01x slower                                                       |
| django_template | 35.6 ms                                                               | 37.8 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo            | 27.3 us                                                               | 25.2 us: 1.08x faster                                                       |
| unpickle_pure_python     | 216 us                                                                | 201 us: 1.08x faster                                                        |
| genshi_text              | 24.2 ms                                                               | 22.8 ms: 1.06x faster                                                       |
| json                     | 5.56 ms                                                               | 5.36 ms: 1.04x faster                                                       |
| regex_dna                | 219 ms                                                                | 212 ms: 1.04x faster                                                        |
| xml_etree_process        | 55.2 ms                                                               | 53.9 ms: 1.03x faster                                                       |
| richards_super           | 45.4 ms                                                               | 44.3 ms: 1.02x faster                                                       |
| chaos                    | 58.7 ms                                                               | 57.5 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed  | 571 ms                                                                | 561 ms: 1.02x faster                                                        |
| async_generators         | 460 ms                                                                | 452 ms: 1.02x faster                                                        |
| coverage                 | 86.5 ms                                                               | 85.2 ms: 1.02x faster                                                       |
| nqueens                  | 85.2 ms                                                               | 84.0 ms: 1.01x faster                                                       |
| pprint_pformat           | 1.52 sec                                                              | 1.50 sec: 1.01x faster                                                      |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                       |
| xml_etree_generate       | 77.8 ms                                                               | 77.2 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| richards                 | 39.2 ms                                                               | 39.4 ms: 1.01x slower                                                       |
| async_tree_io            | 932 ms                                                                | 938 ms: 1.01x slower                                                        |
| create_gc_cycles         | 1.75 ms                                                               | 1.77 ms: 1.01x slower                                                       |
| python_startup_no_site   | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                       |
| spectral_norm            | 99.2 ms                                                               | 100 ms: 1.01x slower                                                        |
| genshi_xml               | 58.1 ms                                                               | 58.7 ms: 1.01x slower                                                       |
| generators               | 32.9 ms                                                               | 33.2 ms: 1.01x slower                                                       |
| scimark_lu               | 109 ms                                                                | 111 ms: 1.01x slower                                                        |
| json_loads               | 28.6 us                                                               | 28.9 us: 1.01x slower                                                       |
| regex_effbot             | 3.55 ms                                                               | 3.59 ms: 1.01x slower                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| pyflate                  | 452 ms                                                                | 458 ms: 1.01x slower                                                        |
| float                    | 70.2 ms                                                               | 71.4 ms: 1.02x slower                                                       |
| nbody                    | 79.1 ms                                                               | 80.7 ms: 1.02x slower                                                       |
| regex_v8                 | 24.8 ms                                                               | 25.3 ms: 1.02x slower                                                       |
| logging_format           | 6.21 us                                                               | 6.36 us: 1.02x slower                                                       |
| telco                    | 7.82 ms                                                               | 8.02 ms: 1.03x slower                                                       |
| scimark_fft              | 303 ms                                                                | 311 ms: 1.03x slower                                                        |
| bpe_tokeniser            | 4.43 sec                                                              | 4.55 sec: 1.03x slower                                                      |
| deltablue                | 3.19 ms                                                               | 3.28 ms: 1.03x slower                                                       |
| typing_runtime_protocols | 163 us                                                                | 168 us: 1.03x slower                                                        |
| pprint_safe_repr         | 724 ms                                                                | 746 ms: 1.03x slower                                                        |
| sqlglot_transpile        | 1.70 ms                                                               | 1.75 ms: 1.03x slower                                                       |
| logging_simple           | 5.70 us                                                               | 5.89 us: 1.03x slower                                                       |
| raytrace                 | 274 ms                                                                | 284 ms: 1.04x slower                                                        |
| async_tree_memoization   | 401 ms                                                                | 416 ms: 1.04x slower                                                        |
| go                       | 130 ms                                                                | 135 ms: 1.04x slower                                                        |
| asyncio_tcp              | 485 ms                                                                | 506 ms: 1.04x slower                                                        |
| scimark_sor              | 116 ms                                                                | 121 ms: 1.04x slower                                                        |
| 2to3                     | 275 ms                                                                | 288 ms: 1.04x slower                                                        |
| html5lib                 | 64.7 ms                                                               | 67.7 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult  | 4.20 ms                                                               | 4.41 ms: 1.05x slower                                                       |
| logging_silent           | 104 ns                                                                | 109 ns: 1.05x slower                                                        |
| sympy_expand             | 504 ms                                                                | 533 ms: 1.06x slower                                                        |
| gc_traversal             | 3.56 ms                                                               | 3.77 ms: 1.06x slower                                                       |
| django_template          | 35.6 ms                                                               | 37.8 ms: 1.06x slower                                                       |
| docutils                 | 3.03 sec                                                              | 3.23 sec: 1.07x slower                                                      |
| sqlglot_optimize         | 57.7 ms                                                               | 61.6 ms: 1.07x slower                                                       |
| tomli_loads              | 1.93 sec                                                              | 2.07 sec: 1.07x slower                                                      |
| sympy_str                | 299 ms                                                                | 322 ms: 1.07x slower                                                        |
| sqlglot_normalize        | 113 ms                                                                | 121 ms: 1.08x slower                                                        |
| hexiom                   | 6.85 ms                                                               | 7.42 ms: 1.08x slower                                                       |
| regex_compile            | 142 ms                                                                | 154 ms: 1.09x slower                                                        |
| tornado_http             | 95.6 ms                                                               | 104 ms: 1.09x slower                                                        |
| pickle_pure_python       | 301 us                                                                | 330 us: 1.09x slower                                                        |
| sympy_integrate          | 22.7 ms                                                               | 24.9 ms: 1.10x slower                                                       |
| dulwich_log              | 68.8 ms                                                               | 75.4 ms: 1.10x slower                                                       |
| sympy_sum                | 173 ms                                                                | 190 ms: 1.10x slower                                                        |
| pylint                   | 372 ms                                                                | 412 ms: 1.11x slower                                                        |
| sqlglot_parse            | 1.34 ms                                                               | 1.49 ms: 1.11x slower                                                       |
| pycparser                | 1.17 sec                                                              | 1.32 sec: 1.13x slower                                                      |
| scimark_monte_carlo      | 62.8 ms                                                               | 71.4 ms: 1.14x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (22): async_tree_cpu_io_mixed_tg, asyncio_websockets, mdp, meteor_contest, mako, json_dumps, bench_mp_pool, pidigits, pathlib, fannkuch, bench_thread_pool, async_tree_none, xml_etree_parse, thrift, xml_etree_iterparse, coroutines, deepcopy, crypto_pyaes, deepcopy_reduce, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (7) of results/bm-20240908-3.14.0a0-e666b14-JIT/bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x