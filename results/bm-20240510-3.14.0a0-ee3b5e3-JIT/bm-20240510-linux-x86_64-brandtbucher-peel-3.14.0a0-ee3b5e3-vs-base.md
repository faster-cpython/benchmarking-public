# Results vs. base

- fork: brandtbucher
- ref: peel
- machine: linux-x86_64
- commit hash: ee3b5e3
- commit date: 2024-05-10
- overall geometric mean: 1.00x slower
- HPT reliability: 69.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| html5lib       | 67.7 ms                                                               | 67.1 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 71.6 ms                                                               | 71.2 ms: 1.01x faster                                       |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                        |
| nbody          | 80.9 ms                                                               | 83.9 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.55 ms                                                               | 3.51 ms: 1.01x faster                                       |
| regex_dna      | 214 ms                                                                | 223 ms: 1.04x slower                                        |
| regex_v8       | 24.3 ms                                                               | 25.3 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 1.95 sec                                                              | 1.94 sec: 1.01x faster                                      |
| xml_etree_process    | 59.1 ms                                                               | 58.7 ms: 1.01x faster                                       |
| json_loads           | 29.1 us                                                               | 29.0 us: 1.00x faster                                       |
| unpickle_list        | 5.44 us                                                               | 5.52 us: 1.01x slower                                       |
| unpickle_pure_python | 222 us                                                                | 227 us: 1.02x slower                                        |
| pickle_list          | 5.47 us                                                               | 5.60 us: 1.02x slower                                       |
| pickle_dict          | 33.5 us                                                               | 35.0 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                |

Benchmark hidden because not significant (7): xml_etree_parse, unpickle, xml_etree_generate, pickle, json_dumps, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                       |
| python_startup_no_site | 7.63 ms                                                               | 7.60 ms: 1.00x faster                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 9.56 ms                                                               | 9.59 ms: 1.00x slower                                       |
| genshi_text    | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240510-linux-x86_64-brandtbucher-peel-3.14.0a0-ee3b5e3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------:|
| scimark_sor             | 136 ms                                                                | 128 ms: 1.06x faster                                        |
| spectral_norm           | 102 ms                                                                | 97.1 ms: 1.05x faster                                       |
| mdp                     | 2.72 sec                                                              | 2.59 sec: 1.05x faster                                      |
| coverage                | 95.1 ms                                                               | 92.0 ms: 1.03x faster                                       |
| fannkuch                | 371 ms                                                                | 359 ms: 1.03x faster                                        |
| pyflate                 | 459 ms                                                                | 449 ms: 1.02x faster                                        |
| json                    | 5.39 ms                                                               | 5.27 ms: 1.02x faster                                       |
| scimark_lu              | 125 ms                                                                | 122 ms: 1.02x faster                                        |
| go                      | 149 ms                                                                | 147 ms: 1.02x faster                                        |
| nqueens                 | 87.0 ms                                                               | 85.9 ms: 1.01x faster                                       |
| dulwich_log             | 69.6 ms                                                               | 68.8 ms: 1.01x faster                                       |
| comprehensions          | 16.7 us                                                               | 16.5 us: 1.01x faster                                       |
| html5lib                | 67.7 ms                                                               | 67.1 ms: 1.01x faster                                       |
| regex_effbot            | 3.55 ms                                                               | 3.51 ms: 1.01x faster                                       |
| tomli_loads             | 1.95 sec                                                              | 1.94 sec: 1.01x faster                                      |
| xml_etree_process       | 59.1 ms                                                               | 58.7 ms: 1.01x faster                                       |
| python_startup          | 11.0 ms                                                               | 10.9 ms: 1.01x faster                                       |
| float                   | 71.6 ms                                                               | 71.2 ms: 1.01x faster                                       |
| asyncio_tcp             | 522 ms                                                                | 520 ms: 1.00x faster                                        |
| deepcopy_memo           | 37.9 us                                                               | 37.8 us: 1.00x faster                                       |
| telco                   | 173 ms                                                                | 172 ms: 1.00x faster                                        |
| python_startup_no_site  | 7.63 ms                                                               | 7.60 ms: 1.00x faster                                       |
| json_loads              | 29.1 us                                                               | 29.0 us: 1.00x faster                                       |
| asyncio_tcp_ssl         | 1.86 sec                                                              | 1.86 sec: 1.00x faster                                      |
| pidigits                | 188 ms                                                                | 189 ms: 1.00x slower                                        |
| mako                    | 9.56 ms                                                               | 9.59 ms: 1.00x slower                                       |
| sqlglot_transpile       | 1.64 ms                                                               | 1.65 ms: 1.01x slower                                       |
| async_generators        | 466 ms                                                                | 469 ms: 1.01x slower                                        |
| create_gc_cycles        | 1.83 ms                                                               | 1.84 ms: 1.01x slower                                       |
| gc_traversal            | 3.87 ms                                                               | 3.90 ms: 1.01x slower                                       |
| raytrace                | 278 ms                                                                | 281 ms: 1.01x slower                                        |
| sympy_str               | 301 ms                                                                | 305 ms: 1.01x slower                                        |
| sympy_sum               | 172 ms                                                                | 174 ms: 1.01x slower                                        |
| sqlglot_optimize        | 56.5 ms                                                               | 57.2 ms: 1.01x slower                                       |
| unpickle_list           | 5.44 us                                                               | 5.52 us: 1.01x slower                                       |
| sympy_integrate         | 22.6 ms                                                               | 22.9 ms: 1.01x slower                                       |
| coroutines              | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                       |
| meteor_contest          | 110 ms                                                                | 112 ms: 1.01x slower                                        |
| sqlglot_normalize       | 112 ms                                                                | 114 ms: 1.02x slower                                        |
| chaos                   | 59.3 ms                                                               | 60.5 ms: 1.02x slower                                       |
| scimark_sparse_mat_mult | 4.49 ms                                                               | 4.58 ms: 1.02x slower                                       |
| logging_simple          | 5.73 us                                                               | 5.85 us: 1.02x slower                                       |
| unpickle_pure_python    | 222 us                                                                | 227 us: 1.02x slower                                        |
| pickle_list             | 5.47 us                                                               | 5.60 us: 1.02x slower                                       |
| genshi_text             | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                       |
| pprint_safe_repr        | 708 ms                                                                | 731 ms: 1.03x slower                                        |
| hexiom                  | 6.58 ms                                                               | 6.80 ms: 1.03x slower                                       |
| logging_format          | 6.28 us                                                               | 6.50 us: 1.04x slower                                       |
| nbody                   | 80.9 ms                                                               | 83.9 ms: 1.04x slower                                       |
| regex_dna               | 214 ms                                                                | 223 ms: 1.04x slower                                        |
| regex_v8                | 24.3 ms                                                               | 25.3 ms: 1.04x slower                                       |
| pickle_dict             | 33.5 us                                                               | 35.0 us: 1.05x slower                                       |
| pprint_pformat          | 1.45 sec                                                              | 1.53 sec: 1.05x slower                                      |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                |

Benchmark hidden because not significant (44): richards, scimark_monte_carlo, async_tree_none_tg, async_tree_cpu_io_mixed, sqlite_synth, async_tree_memoization, async_tree_cpu_io_mixed_tg, xml_etree_parse, async_tree_none, chameleon, deepcopy_reduce, async_tree_memoization_tg, logging_silent, deltablue, pathlib, 2to3, async_tree_io_tg, generators, django_template, tornado_http, sqlglot_parse, scimark_fft, sympy_expand, unpickle, xml_etree_generate, bench_thread_pool, richards_super, regex_compile, asyncio_websockets, pickle, json_dumps, thrift, xml_etree_iterparse, pickle_pure_python, bench_mp_pool, flaskblogging, typing_runtime_protocols, genshi_xml, crypto_pyaes, dask, pylint, pycparser, deepcopy, async_tree_io
Ignored benchmarks (1) of results/bm-20240510-3.14.0a0-ec9d12b-JIT/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: docutils

# HPT report

- Reliability score: 69.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x