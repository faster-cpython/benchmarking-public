# Results vs. base

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 285 ms: 1.03x slower                                                        |
| docutils       | 3.03 sec                                                              | 3.25 sec: 1.07x slower                                                      |
| html5lib       | 64.7 ms                                                               | 69.1 ms: 1.07x slower                                                       |
| tornado_http   | 95.6 ms                                                               | 103 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 571 ms                                                                | 563 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| coroutines              | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                       |
| asyncio_tcp             | 485 ms                                                                | 500 ms: 1.03x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_websockets, async_generators, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                                        |
| nbody          | 79.1 ms                                                               | 79.6 ms: 1.01x slower                                                       |
| float          | 70.2 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 216 ms: 1.01x faster                                                        |
| regex_v8       | 24.8 ms                                                               | 24.6 ms: 1.01x faster                                                       |
| regex_effbot   | 3.55 ms                                                               | 3.62 ms: 1.02x slower                                                       |
| regex_compile  | 142 ms                                                                | 151 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                | 201 us: 1.07x faster                                                        |
| xml_etree_process    | 55.2 ms                                                               | 54.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 98.0 ms                                                               | 98.7 ms: 1.01x slower                                                       |
| xml_etree_parse      | 145 ms                                                                | 148 ms: 1.02x slower                                                        |
| pickle_pure_python   | 301 us                                                                | 310 us: 1.03x slower                                                        |
| tomli_loads          | 1.93 sec                                                              | 2.00 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (3): json_loads, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                       |
| mako            | 9.77 ms                                                               | 9.70 ms: 1.01x faster                                                       |
| django_template | 35.6 ms                                                               | 37.9 ms: 1.06x slower                                                       |
| genshi_xml      | 58.1 ms                                                               | 63.5 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python    | 216 us                                                                | 201 us: 1.07x faster                                                        |
| logging_silent          | 104 ns                                                                | 97.3 ns: 1.07x faster                                                       |
| richards_super          | 45.4 ms                                                               | 42.8 ms: 1.06x faster                                                       |
| json                    | 5.56 ms                                                               | 5.27 ms: 1.05x faster                                                       |
| deepcopy_memo           | 27.3 us                                                               | 26.0 us: 1.05x faster                                                       |
| richards                | 39.2 ms                                                               | 38.4 ms: 1.02x faster                                                       |
| nqueens                 | 85.2 ms                                                               | 83.8 ms: 1.02x faster                                                       |
| xml_etree_process       | 55.2 ms                                                               | 54.3 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 2.68 us                                                               | 2.64 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 571 ms                                                                | 563 ms: 1.01x faster                                                        |
| regex_dna               | 219 ms                                                                | 216 ms: 1.01x faster                                                        |
| genshi_text             | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                       |
| deepcopy                | 266 us                                                                | 263 us: 1.01x faster                                                        |
| comprehensions          | 16.7 us                                                               | 16.5 us: 1.01x faster                                                       |
| pidigits                | 187 ms                                                                | 185 ms: 1.01x faster                                                        |
| crypto_pyaes            | 65.9 ms                                                               | 65.4 ms: 1.01x faster                                                       |
| regex_v8                | 24.8 ms                                                               | 24.6 ms: 1.01x faster                                                       |
| mako                    | 9.77 ms                                                               | 9.70 ms: 1.01x faster                                                       |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.00x slower                                                        |
| bpe_tokeniser           | 4.43 sec                                                              | 4.45 sec: 1.00x slower                                                      |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                      |
| nbody                   | 79.1 ms                                                               | 79.6 ms: 1.01x slower                                                       |
| raytrace                | 274 ms                                                                | 275 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 98.0 ms                                                               | 98.7 ms: 1.01x slower                                                       |
| float                   | 70.2 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| python_startup_no_site  | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                       |
| generators              | 32.9 ms                                                               | 33.2 ms: 1.01x slower                                                       |
| bench_thread_pool       | 836 us                                                                | 846 us: 1.01x slower                                                        |
| python_startup          | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| xml_etree_parse         | 145 ms                                                                | 148 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                       |
| deltablue               | 3.19 ms                                                               | 3.24 ms: 1.02x slower                                                       |
| pprint_safe_repr        | 724 ms                                                                | 738 ms: 1.02x slower                                                        |
| coroutines              | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                       |
| regex_effbot            | 3.55 ms                                                               | 3.62 ms: 1.02x slower                                                       |
| scimark_fft             | 303 ms                                                                | 309 ms: 1.02x slower                                                        |
| pyflate                 | 452 ms                                                                | 462 ms: 1.02x slower                                                        |
| fannkuch                | 372 ms                                                                | 382 ms: 1.03x slower                                                        |
| pickle_pure_python      | 301 us                                                                | 310 us: 1.03x slower                                                        |
| asyncio_tcp             | 485 ms                                                                | 500 ms: 1.03x slower                                                        |
| logging_format          | 6.21 us                                                               | 6.42 us: 1.03x slower                                                       |
| 2to3                    | 275 ms                                                                | 285 ms: 1.03x slower                                                        |
| tomli_loads             | 1.93 sec                                                              | 2.00 sec: 1.04x slower                                                      |
| logging_simple          | 5.70 us                                                               | 5.91 us: 1.04x slower                                                       |
| sqlglot_optimize        | 57.7 ms                                                               | 60.1 ms: 1.04x slower                                                       |
| scimark_lu              | 109 ms                                                                | 115 ms: 1.05x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                               | 1.78 ms: 1.05x slower                                                       |
| sympy_expand            | 504 ms                                                                | 530 ms: 1.05x slower                                                        |
| go                      | 130 ms                                                                | 138 ms: 1.06x slower                                                        |
| sqlglot_normalize       | 113 ms                                                                | 119 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult | 4.20 ms                                                               | 4.44 ms: 1.06x slower                                                       |
| gc_traversal            | 3.56 ms                                                               | 3.78 ms: 1.06x slower                                                       |
| django_template         | 35.6 ms                                                               | 37.9 ms: 1.06x slower                                                       |
| regex_compile           | 142 ms                                                                | 151 ms: 1.06x slower                                                        |
| scimark_sor             | 116 ms                                                                | 124 ms: 1.07x slower                                                        |
| sympy_str               | 299 ms                                                                | 319 ms: 1.07x slower                                                        |
| html5lib                | 64.7 ms                                                               | 69.1 ms: 1.07x slower                                                       |
| scimark_monte_carlo     | 62.8 ms                                                               | 67.4 ms: 1.07x slower                                                       |
| docutils                | 3.03 sec                                                              | 3.25 sec: 1.07x slower                                                      |
| dulwich_log             | 68.8 ms                                                               | 74.1 ms: 1.08x slower                                                       |
| tornado_http            | 95.6 ms                                                               | 103 ms: 1.08x slower                                                        |
| pycparser               | 1.17 sec                                                              | 1.27 sec: 1.09x slower                                                      |
| genshi_xml              | 58.1 ms                                                               | 63.5 ms: 1.09x slower                                                       |
| sympy_sum               | 173 ms                                                                | 189 ms: 1.09x slower                                                        |
| sympy_integrate         | 22.7 ms                                                               | 24.9 ms: 1.10x slower                                                       |
| pylint                  | 372 ms                                                                | 416 ms: 1.12x slower                                                        |
| sqlglot_parse           | 1.34 ms                                                               | 1.52 ms: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (23): async_tree_cpu_io_mixed_tg, async_tree_none_tg, chaos, pprint_pformat, pathlib, mdp, asyncio_websockets, json_loads, xml_etree_generate, thrift, async_generators, async_tree_io_tg, bench_mp_pool, async_tree_none, telco, async_tree_memoization_tg, hexiom, async_tree_io, typing_runtime_protocols, json_dumps, coverage, spectral_norm, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240906-3.14.0a0-7ad3776-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x