# Results vs. base

- fork: brandtbucher
- ref: yes_underflow
- machine: linux-x86_64
- commit hash: 4112331
- commit date: 2025-02-14
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 260 ms: 1.00x faster                                                  |
| html5lib       | 63.3 ms                                                                | 69.0 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators       | 411 ms                                                                 | 412 ms: 1.00x slower                                                  |
| async_tree_memoization | 327 ms                                                                 | 329 ms: 1.01x slower                                                  |
| coroutines             | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 67.2 ms                                                                | 66.0 ms: 1.02x faster                                                 |
| nbody          | 90.4 ms                                                                | 89.3 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.18 ms                                                                | 3.05 ms: 1.04x faster                                                 |
| regex_dna      | 211 ms                                                                 | 202 ms: 1.04x faster                                                  |
| regex_v8       | 24.0 ms                                                                | 24.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 78.0 ms                                                                | 78.8 ms: 1.01x slower                                                 |
| xml_etree_iterparse | 94.7 ms                                                                | 96.1 ms: 1.01x slower                                                 |
| json_dumps          | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                 |
| xml_etree_process   | 54.6 ms                                                                | 55.7 ms: 1.02x slower                                                 |
| tomli_loads         | 1.84 sec                                                               | 1.98 sec: 1.08x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                 |
| python_startup_no_site | 7.06 ms                                                                | 7.06 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.3 ms                                                                | 9.95 ms: 1.03x faster                                                 |
| django_template | 33.1 ms                                                                | 35.7 ms: 1.08x slower                                                 |
| genshi_xml      | 57.7 ms                                                                | 66.7 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 3.18 ms                                                                | 3.05 ms: 1.04x faster                                                 |
| regex_dna               | 211 ms                                                                 | 202 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult | 4.63 ms                                                                | 4.45 ms: 1.04x faster                                                 |
| mako                    | 10.3 ms                                                                | 9.95 ms: 1.03x faster                                                 |
| spectral_norm           | 95.6 ms                                                                | 93.0 ms: 1.03x faster                                                 |
| gc_traversal            | 4.77 ms                                                                | 4.65 ms: 1.03x faster                                                 |
| nqueens                 | 89.5 ms                                                                | 87.9 ms: 1.02x faster                                                 |
| float                   | 67.2 ms                                                                | 66.0 ms: 1.02x faster                                                 |
| deepcopy_memo           | 30.2 us                                                                | 29.8 us: 1.02x faster                                                 |
| pathlib                 | 16.1 ms                                                                | 15.8 ms: 1.01x faster                                                 |
| nbody                   | 90.4 ms                                                                | 89.3 ms: 1.01x faster                                                 |
| scimark_monte_carlo     | 63.9 ms                                                                | 63.4 ms: 1.01x faster                                                 |
| sqlalchemy_imperative   | 16.8 ms                                                                | 16.7 ms: 1.01x faster                                                 |
| scimark_fft             | 314 ms                                                                 | 312 ms: 1.01x faster                                                  |
| bench_thread_pool       | 894 us                                                                 | 890 us: 1.00x faster                                                  |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| 2to3                    | 261 ms                                                                 | 260 ms: 1.00x faster                                                  |
| python_startup          | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                 |
| meteor_contest          | 108 ms                                                                 | 108 ms: 1.00x faster                                                  |
| python_startup_no_site  | 7.06 ms                                                                | 7.06 ms: 1.00x faster                                                 |
| shortest_path           | 481 ms                                                                 | 482 ms: 1.00x slower                                                  |
| async_generators        | 411 ms                                                                 | 412 ms: 1.00x slower                                                  |
| bpe_tokeniser           | 4.36 sec                                                               | 4.38 sec: 1.00x slower                                                |
| sympy_expand            | 470 ms                                                                 | 472 ms: 1.00x slower                                                  |
| sympy_str               | 279 ms                                                                 | 281 ms: 1.01x slower                                                  |
| coverage                | 89.7 ms                                                                | 90.3 ms: 1.01x slower                                                 |
| many_optionals          | 958 us                                                                 | 964 us: 1.01x slower                                                  |
| async_tree_memoization  | 327 ms                                                                 | 329 ms: 1.01x slower                                                  |
| create_gc_cycles        | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                 |
| mdp                     | 2.54 sec                                                               | 2.57 sec: 1.01x slower                                                |
| sqlglot_transpile       | 1.58 ms                                                                | 1.60 ms: 1.01x slower                                                 |
| regex_v8                | 24.0 ms                                                                | 24.2 ms: 1.01x slower                                                 |
| xml_etree_generate      | 78.0 ms                                                                | 78.8 ms: 1.01x slower                                                 |
| sqlglot_optimize        | 54.1 ms                                                                | 54.7 ms: 1.01x slower                                                 |
| fannkuch                | 392 ms                                                                 | 397 ms: 1.01x slower                                                  |
| comprehensions          | 17.1 us                                                                | 17.4 us: 1.01x slower                                                 |
| xml_etree_iterparse     | 94.7 ms                                                                | 96.1 ms: 1.01x slower                                                 |
| pyflate                 | 463 ms                                                                 | 471 ms: 1.02x slower                                                  |
| json_dumps              | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                 |
| deepcopy_reduce         | 2.73 us                                                                | 2.79 us: 1.02x slower                                                 |
| subparsers              | 20.7 ms                                                                | 21.1 ms: 1.02x slower                                                 |
| xml_etree_process       | 54.6 ms                                                                | 55.7 ms: 1.02x slower                                                 |
| sqlglot_parse           | 1.28 ms                                                                | 1.31 ms: 1.02x slower                                                 |
| hexiom                  | 7.46 ms                                                                | 7.68 ms: 1.03x slower                                                 |
| coroutines              | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                 |
| deepcopy                | 265 us                                                                 | 274 us: 1.03x slower                                                  |
| scimark_sor             | 114 ms                                                                 | 119 ms: 1.05x slower                                                  |
| chaos                   | 58.8 ms                                                                | 61.5 ms: 1.05x slower                                                 |
| dulwich_log             | 66.8 ms                                                                | 70.5 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 728 ms                                                                 | 770 ms: 1.06x slower                                                  |
| pprint_pformat          | 1.50 sec                                                               | 1.59 sec: 1.06x slower                                                |
| sqlglot_normalize       | 108 ms                                                                 | 115 ms: 1.06x slower                                                  |
| scimark_lu              | 113 ms                                                                 | 120 ms: 1.06x slower                                                  |
| tomli_loads             | 1.84 sec                                                               | 1.98 sec: 1.08x slower                                                |
| pycparser               | 1.14 sec                                                               | 1.23 sec: 1.08x slower                                                |
| django_template         | 33.1 ms                                                                | 35.7 ms: 1.08x slower                                                 |
| html5lib                | 63.3 ms                                                                | 69.0 ms: 1.09x slower                                                 |
| go                      | 128 ms                                                                 | 141 ms: 1.10x slower                                                  |
| logging_format          | 6.17 us                                                                | 6.83 us: 1.11x slower                                                 |
| logging_simple          | 5.63 us                                                                | 6.27 us: 1.11x slower                                                 |
| genshi_xml              | 57.7 ms                                                                | 66.7 ms: 1.16x slower                                                 |
| deltablue               | 3.49 ms                                                                | 4.22 ms: 1.21x slower                                                 |
| logging_silent          | 108 ns                                                                 | 134 ns: 1.24x slower                                                  |
| generators              | 37.5 ms                                                                | 49.5 ms: 1.32x slower                                                 |
| richards                | 43.5 ms                                                                | 64.2 ms: 1.48x slower                                                 |
| richards_super          | 49.7 ms                                                                | 75.9 ms: 1.53x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (30): async_tree_io_tg, typing_runtime_protocols, crypto_pyaes, thrift, async_tree_cpu_io_mixed, async_tree_memoization_tg, telco, sympy_integrate, regex_compile, docutils, sqlite_synth, raytrace, genshi_text, sqlalchemy_declarative, xml_etree_parse, bench_mp_pool, pylint, asyncio_websockets, async_tree_cpu_io_mixed_tg, connected_components, pickle_pure_python, json_loads, sympy_sum, async_tree_none_tg, sphinx, k_core, json, unpickle_pure_python, async_tree_io, async_tree_none

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x