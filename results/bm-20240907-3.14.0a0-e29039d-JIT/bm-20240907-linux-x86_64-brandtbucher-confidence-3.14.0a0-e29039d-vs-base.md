# Results vs. base

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.00x faster
- HPT reliability: 98.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 275 ms: 1.00x faster                                              |
| docutils       | 3.03 sec                                                              | 3.01 sec: 1.01x faster                                            |
| html5lib       | 64.7 ms                                                               | 64.3 ms: 1.01x faster                                             |
| tornado_http   | 95.6 ms                                                               | 94.9 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines              | 22.8 ms                                                               | 22.3 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed | 571 ms                                                                | 565 ms: 1.01x faster                                              |
| async_generators        | 460 ms                                                                | 456 ms: 1.01x faster                                              |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                            |
| asyncio_tcp             | 485 ms                                                                | 488 ms: 1.01x slower                                              |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.01x faster                                              |
| nbody          | 79.1 ms                                                               | 79.5 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                | 139 ms: 1.02x faster                                              |
| regex_v8       | 24.8 ms                                                               | 24.8 ms: 1.00x faster                                             |
| regex_dna      | 219 ms                                                                | 222 ms: 1.01x slower                                              |
| regex_effbot   | 3.55 ms                                                               | 3.78 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 211 us: 1.02x faster                                              |
| xml_etree_process    | 55.2 ms                                                               | 54.8 ms: 1.01x faster                                             |
| tomli_loads          | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                            |
| xml_etree_generate   | 77.8 ms                                                               | 77.3 ms: 1.01x faster                                             |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                             |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                               | 56.7 ms: 1.02x faster                                             |
| genshi_text    | 24.2 ms                                                               | 24.0 ms: 1.01x faster                                             |
| mako           | 9.77 ms                                                               | 9.84 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| richards_super           | 45.4 ms                                                               | 43.0 ms: 1.06x faster                                             |
| json                     | 5.56 ms                                                               | 5.32 ms: 1.05x faster                                             |
| pyflate                  | 452 ms                                                                | 432 ms: 1.05x faster                                              |
| pprint_pformat           | 1.52 sec                                                              | 1.47 sec: 1.03x faster                                            |
| genshi_xml               | 58.1 ms                                                               | 56.7 ms: 1.02x faster                                             |
| unpickle_pure_python     | 216 us                                                                | 211 us: 1.02x faster                                              |
| logging_silent           | 104 ns                                                                | 102 ns: 1.02x faster                                              |
| coroutines               | 22.8 ms                                                               | 22.3 ms: 1.02x faster                                             |
| deepcopy_memo            | 27.3 us                                                               | 26.8 us: 1.02x faster                                             |
| scimark_sor              | 116 ms                                                                | 114 ms: 1.02x faster                                              |
| regex_compile            | 142 ms                                                                | 139 ms: 1.02x faster                                              |
| sqlglot_transpile        | 1.70 ms                                                               | 1.67 ms: 1.02x faster                                             |
| sqlglot_parse            | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed  | 571 ms                                                                | 565 ms: 1.01x faster                                              |
| async_generators         | 460 ms                                                                | 456 ms: 1.01x faster                                              |
| richards                 | 39.2 ms                                                               | 38.9 ms: 1.01x faster                                             |
| pidigits                 | 187 ms                                                                | 186 ms: 1.01x faster                                              |
| xml_etree_process        | 55.2 ms                                                               | 54.8 ms: 1.01x faster                                             |
| sympy_sum                | 173 ms                                                                | 172 ms: 1.01x faster                                              |
| docutils                 | 3.03 sec                                                              | 3.01 sec: 1.01x faster                                            |
| tomli_loads              | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                            |
| tornado_http             | 95.6 ms                                                               | 94.9 ms: 1.01x faster                                             |
| xml_etree_generate       | 77.8 ms                                                               | 77.3 ms: 1.01x faster                                             |
| genshi_text              | 24.2 ms                                                               | 24.0 ms: 1.01x faster                                             |
| html5lib                 | 64.7 ms                                                               | 64.3 ms: 1.01x faster                                             |
| go                       | 130 ms                                                                | 130 ms: 1.00x faster                                              |
| sympy_str                | 299 ms                                                                | 298 ms: 1.00x faster                                              |
| hexiom                   | 6.85 ms                                                               | 6.83 ms: 1.00x faster                                             |
| 2to3                     | 275 ms                                                                | 275 ms: 1.00x faster                                              |
| bpe_tokeniser            | 4.43 sec                                                              | 4.41 sec: 1.00x faster                                            |
| regex_v8                 | 24.8 ms                                                               | 24.8 ms: 1.00x faster                                             |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                            |
| nbody                    | 79.1 ms                                                               | 79.5 ms: 1.00x slower                                             |
| create_gc_cycles         | 1.75 ms                                                               | 1.76 ms: 1.00x slower                                             |
| sqlglot_optimize         | 57.7 ms                                                               | 57.9 ms: 1.00x slower                                             |
| asyncio_tcp              | 485 ms                                                                | 488 ms: 1.01x slower                                              |
| python_startup_no_site   | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                             |
| typing_runtime_protocols | 163 us                                                                | 164 us: 1.01x slower                                              |
| mako                     | 9.77 ms                                                               | 9.84 ms: 1.01x slower                                             |
| deltablue                | 3.19 ms                                                               | 3.22 ms: 1.01x slower                                             |
| deepcopy                 | 266 us                                                                | 269 us: 1.01x slower                                              |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                             |
| regex_dna                | 219 ms                                                                | 222 ms: 1.01x slower                                              |
| pathlib                  | 15.9 ms                                                               | 16.2 ms: 1.02x slower                                             |
| mdp                      | 2.54 sec                                                              | 2.60 sec: 1.02x slower                                            |
| scimark_fft              | 303 ms                                                                | 311 ms: 1.02x slower                                              |
| pycparser                | 1.17 sec                                                              | 1.20 sec: 1.03x slower                                            |
| scimark_sparse_mat_mult  | 4.20 ms                                                               | 4.36 ms: 1.04x slower                                             |
| gc_traversal             | 3.56 ms                                                               | 3.74 ms: 1.05x slower                                             |
| regex_effbot             | 3.55 ms                                                               | 3.78 ms: 1.07x slower                                             |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (40): async_tree_memoization, async_tree_cpu_io_mixed_tg, pprint_safe_repr, coverage, spectral_norm, async_tree_memoization_tg, deepcopy_reduce, async_tree_io_tg, logging_format, pickle_pure_python, chaos, asyncio_websockets, dulwich_log, logging_simple, async_tree_none_tg, django_template, pylint, telco, xml_etree_parse, sqlglot_normalize, sympy_integrate, bench_mp_pool, json_loads, bench_thread_pool, async_tree_none, async_tree_io, comprehensions, generators, fannkuch, float, crypto_pyaes, thrift, json_dumps, meteor_contest, sympy_expand, scimark_lu, raytrace, xml_etree_iterparse, nqueens, scimark_monte_carlo
Ignored benchmarks (7) of results/bm-20240907-3.14.0a0-e29039d-JIT/bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x