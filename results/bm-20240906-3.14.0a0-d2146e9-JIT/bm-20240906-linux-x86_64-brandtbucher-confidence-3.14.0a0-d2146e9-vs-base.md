# Results vs. base

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d2146e9
- commit date: 2024-09-06
- overall geometric mean: 1.000x faster
- HPT reliability: 71.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 3.03 sec                                                              | 3.00 sec: 1.01x faster                                            |
| html5lib       | 64.7 ms                                                               | 62.3 ms: 1.04x faster                                             |
| tornado_http   | 95.6 ms                                                               | 96.1 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io   | 932 ms                                                                | 929 ms: 1.00x faster                                              |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (11): async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_generators, asyncio_websockets, async_tree_none, coroutines, async_tree_none_tg, asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                              |
| float          | 70.2 ms                                                               | 70.7 ms: 1.01x slower                                             |
| nbody          | 79.1 ms                                                               | 81.2 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 210 ms: 1.04x faster                                              |
| regex_v8       | 24.8 ms                                                               | 24.0 ms: 1.03x faster                                             |
| regex_effbot   | 3.55 ms                                                               | 3.50 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 213 us: 1.01x faster                                              |
| xml_etree_generate   | 77.8 ms                                                               | 78.3 ms: 1.01x slower                                             |
| xml_etree_iterparse  | 98.0 ms                                                               | 98.8 ms: 1.01x slower                                             |
| pickle_pure_python   | 301 us                                                                | 304 us: 1.01x slower                                              |
| xml_etree_parse      | 145 ms                                                                | 148 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_process, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                             |
| python_startup         | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                               | 58.7 ms: 1.01x slower                                             |
| genshi_text    | 24.2 ms                                                               | 24.4 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pyflate                 | 452 ms                                                                | 424 ms: 1.06x faster                                              |
| richards_super          | 45.4 ms                                                               | 42.9 ms: 1.06x faster                                             |
| regex_dna               | 219 ms                                                                | 210 ms: 1.04x faster                                              |
| pprint_pformat          | 1.52 sec                                                              | 1.46 sec: 1.04x faster                                            |
| json                    | 5.56 ms                                                               | 5.35 ms: 1.04x faster                                             |
| html5lib                | 64.7 ms                                                               | 62.3 ms: 1.04x faster                                             |
| pprint_safe_repr        | 724 ms                                                                | 700 ms: 1.03x faster                                              |
| logging_simple          | 5.70 us                                                               | 5.52 us: 1.03x faster                                             |
| regex_v8                | 24.8 ms                                                               | 24.0 ms: 1.03x faster                                             |
| logging_silent          | 104 ns                                                                | 101 ns: 1.03x faster                                              |
| logging_format          | 6.21 us                                                               | 6.12 us: 1.02x faster                                             |
| unpickle_pure_python    | 216 us                                                                | 213 us: 1.01x faster                                              |
| regex_effbot            | 3.55 ms                                                               | 3.50 ms: 1.01x faster                                             |
| richards                | 39.2 ms                                                               | 38.7 ms: 1.01x faster                                             |
| deepcopy_memo           | 27.3 us                                                               | 27.0 us: 1.01x faster                                             |
| pidigits                | 187 ms                                                                | 185 ms: 1.01x faster                                              |
| docutils                | 3.03 sec                                                              | 3.00 sec: 1.01x faster                                            |
| sqlglot_transpile       | 1.70 ms                                                               | 1.68 ms: 1.01x faster                                             |
| sqlglot_parse           | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                             |
| scimark_sor             | 116 ms                                                                | 116 ms: 1.01x faster                                              |
| comprehensions          | 16.7 us                                                               | 16.6 us: 1.00x faster                                             |
| async_tree_io           | 932 ms                                                                | 929 ms: 1.00x faster                                              |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                            |
| bench_thread_pool       | 836 us                                                                | 839 us: 1.00x slower                                              |
| sympy_integrate         | 22.7 ms                                                               | 22.8 ms: 1.00x slower                                             |
| go                      | 130 ms                                                                | 131 ms: 1.00x slower                                              |
| tornado_http            | 95.6 ms                                                               | 96.1 ms: 1.01x slower                                             |
| xml_etree_generate      | 77.8 ms                                                               | 78.3 ms: 1.01x slower                                             |
| float                   | 70.2 ms                                                               | 70.7 ms: 1.01x slower                                             |
| sympy_sum               | 173 ms                                                                | 174 ms: 1.01x slower                                              |
| crypto_pyaes            | 65.9 ms                                                               | 66.4 ms: 1.01x slower                                             |
| scimark_lu              | 109 ms                                                                | 110 ms: 1.01x slower                                              |
| python_startup_no_site  | 7.11 ms                                                               | 7.16 ms: 1.01x slower                                             |
| xml_etree_iterparse     | 98.0 ms                                                               | 98.8 ms: 1.01x slower                                             |
| thrift                  | 781 us                                                                | 787 us: 1.01x slower                                              |
| dulwich_log             | 68.8 ms                                                               | 69.4 ms: 1.01x slower                                             |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                              |
| create_gc_cycles        | 1.75 ms                                                               | 1.77 ms: 1.01x slower                                             |
| pickle_pure_python      | 301 us                                                                | 304 us: 1.01x slower                                              |
| genshi_xml              | 58.1 ms                                                               | 58.7 ms: 1.01x slower                                             |
| generators              | 32.9 ms                                                               | 33.2 ms: 1.01x slower                                             |
| sympy_str               | 299 ms                                                                | 302 ms: 1.01x slower                                              |
| sqlglot_optimize        | 57.7 ms                                                               | 58.3 ms: 1.01x slower                                             |
| genshi_text             | 24.2 ms                                                               | 24.4 ms: 1.01x slower                                             |
| python_startup          | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                             |
| sympy_expand            | 504 ms                                                                | 511 ms: 1.01x slower                                              |
| xml_etree_parse         | 145 ms                                                                | 148 ms: 1.02x slower                                              |
| nbody                   | 79.1 ms                                                               | 81.2 ms: 1.03x slower                                             |
| scimark_fft             | 303 ms                                                                | 312 ms: 1.03x slower                                              |
| spectral_norm           | 99.2 ms                                                               | 103 ms: 1.03x slower                                              |
| scimark_sparse_mat_mult | 4.20 ms                                                               | 4.43 ms: 1.06x slower                                             |
| gc_traversal            | 3.56 ms                                                               | 3.77 ms: 1.06x slower                                             |
| mdp                     | 2.54 sec                                                              | 2.73 sec: 1.08x slower                                            |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (37): async_tree_memoization, chaos, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, django_template, async_generators, tomli_loads, fannkuch, hexiom, asyncio_websockets, xml_etree_process, nqueens, bench_mp_pool, sqlglot_normalize, async_tree_none, coroutines, async_tree_none_tg, telco, 2to3, json_loads, bpe_tokeniser, asyncio_tcp, regex_compile, scimark_monte_carlo, mako, pycparser, coverage, pylint, pathlib, deepcopy, json_dumps, deepcopy_reduce, raytrace, deltablue, async_tree_memoization_tg, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240906-3.14.0a0-d2146e9-JIT/bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 71.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x