# Results vs. 3.13.0b2

- fork: nohlson
- ref: 1_investigate_compil
- machine: linux-x86_64
- commit hash: 5b8a44e
- commit date: 2024-06-18
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 267 ms: 1.03x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                 |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 638 ms: 1.04x slower                                                   |
| Geometric mean          | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.6 ms: 1.02x faster                                                  |
| nbody          | 88.3 ms                                                    | 87.4 ms: 1.01x faster                                                  |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| regex_dna      | 221 ms                                                     | 231 ms: 1.04x slower                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.92 ms: 1.07x slower                                                  |
| regex_v8       | 25.1 ms                                                    | 27.2 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                      | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.1 us: 1.03x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 34.0 us: 1.02x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                                  |
| pickle_list          | 5.11 us                                                    | 5.04 us: 1.01x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                   |
| unpickle             | 15.1 us                                                    | 15.3 us: 1.01x slower                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.53 us: 1.03x slower                                                  |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.2 ms                                                    | 11.0 ms: 1.03x faster                                                  |
| genshi_xml     | 51.6 ms                                                    | 50.7 ms: 1.02x faster                                                  |
| genshi_text    | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                | 367 us                                                     | 263 us: 1.40x faster                                                   |
| deepcopy_memo           | 39.7 us                                                    | 29.0 us: 1.37x faster                                                  |
| deepcopy_reduce         | 3.35 us                                                    | 2.71 us: 1.24x faster                                                  |
| gc_traversal            | 3.98 ms                                                    | 3.60 ms: 1.10x faster                                                  |
| scimark_fft             | 392 ms                                                     | 357 ms: 1.10x faster                                                   |
| mdp                     | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                 |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 4.83 ms: 1.09x faster                                                  |
| richards                | 50.9 ms                                                    | 46.8 ms: 1.09x faster                                                  |
| richards_super          | 57.4 ms                                                    | 53.2 ms: 1.08x faster                                                  |
| logging_silent          | 105 ns                                                     | 97.4 ns: 1.07x faster                                                  |
| pathlib                 | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                  |
| scimark_lu              | 122 ms                                                     | 114 ms: 1.07x faster                                                   |
| scimark_monte_carlo     | 69.2 ms                                                    | 66.0 ms: 1.05x faster                                                  |
| fannkuch                | 402 ms                                                     | 385 ms: 1.04x faster                                                   |
| crypto_pyaes            | 77.5 ms                                                    | 74.2 ms: 1.04x faster                                                  |
| scimark_sor             | 127 ms                                                     | 122 ms: 1.04x faster                                                   |
| thrift                  | 823 us                                                     | 791 us: 1.04x faster                                                   |
| chaos                   | 61.3 ms                                                    | 59.0 ms: 1.04x faster                                                  |
| raytrace                | 267 ms                                                     | 257 ms: 1.04x faster                                                   |
| dulwich_log             | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                  |
| create_gc_cycles        | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                  |
| go                      | 145 ms                                                     | 140 ms: 1.03x faster                                                   |
| xml_etree_process       | 61.2 ms                                                    | 59.2 ms: 1.03x faster                                                  |
| html5lib                | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                  |
| spectral_norm           | 116 ms                                                     | 113 ms: 1.03x faster                                                   |
| regex_compile           | 137 ms                                                     | 133 ms: 1.03x faster                                                   |
| unpickle_pure_python    | 218 us                                                     | 212 us: 1.03x faster                                                   |
| sqlite_synth            | 2.99 us                                                    | 2.91 us: 1.03x faster                                                  |
| json_loads              | 28.9 us                                                    | 28.1 us: 1.03x faster                                                  |
| nqueens                 | 81.4 ms                                                    | 79.3 ms: 1.03x faster                                                  |
| logging_format          | 6.47 us                                                    | 6.30 us: 1.03x faster                                                  |
| 2to3                    | 274 ms                                                     | 267 ms: 1.03x faster                                                   |
| mako                    | 11.2 ms                                                    | 11.0 ms: 1.03x faster                                                  |
| bpe_tokeniser           | 5.02 sec                                                   | 4.91 sec: 1.02x faster                                                 |
| pickle_dict             | 34.8 us                                                    | 34.0 us: 1.02x faster                                                  |
| xml_etree_parse         | 162 ms                                                     | 159 ms: 1.02x faster                                                   |
| xml_etree_generate      | 87.4 ms                                                    | 85.7 ms: 1.02x faster                                                  |
| genshi_xml              | 51.6 ms                                                    | 50.7 ms: 1.02x faster                                                  |
| docutils                | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                 |
| sqlglot_optimize        | 55.5 ms                                                    | 54.6 ms: 1.02x faster                                                  |
| asyncio_tcp             | 508 ms                                                     | 500 ms: 1.02x faster                                                   |
| float                   | 78.9 ms                                                    | 77.6 ms: 1.02x faster                                                  |
| sqlglot_transpile       | 1.63 ms                                                    | 1.61 ms: 1.02x faster                                                  |
| hexiom                  | 6.30 ms                                                    | 6.20 ms: 1.02x faster                                                  |
| sympy_str               | 282 ms                                                     | 278 ms: 1.02x faster                                                   |
| meteor_contest          | 110 ms                                                     | 108 ms: 1.01x faster                                                   |
| tornado_http            | 94.6 ms                                                    | 93.3 ms: 1.01x faster                                                  |
| sympy_integrate         | 20.5 ms                                                    | 20.3 ms: 1.01x faster                                                  |
| pickle_list             | 5.11 us                                                    | 5.04 us: 1.01x faster                                                  |
| generators              | 29.6 ms                                                    | 29.3 ms: 1.01x faster                                                  |
| genshi_text             | 23.7 ms                                                    | 23.4 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 110 ms                                                     | 109 ms: 1.01x faster                                                   |
| sqlglot_parse           | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                  |
| nbody                   | 88.3 ms                                                    | 87.4 ms: 1.01x faster                                                  |
| pickle_pure_python      | 305 us                                                     | 302 us: 1.01x faster                                                   |
| sympy_sum               | 156 ms                                                     | 154 ms: 1.01x faster                                                   |
| deltablue               | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                  |
| pyflate                 | 484 ms                                                     | 480 ms: 1.01x faster                                                   |
| pidigits                | 191 ms                                                     | 190 ms: 1.01x faster                                                   |
| bench_thread_pool       | 834 us                                                     | 828 us: 1.01x faster                                                   |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.84 sec: 1.00x faster                                                 |
| python_startup          | 10.8 ms                                                    | 10.7 ms: 1.00x faster                                                  |
| python_startup_no_site  | 7.11 ms                                                    | 7.15 ms: 1.01x slower                                                  |
| pprint_pformat          | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                 |
| unpickle                | 15.1 us                                                    | 15.3 us: 1.01x slower                                                  |
| async_generators        | 442 ms                                                     | 448 ms: 1.01x slower                                                   |
| tomli_loads             | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                 |
| unpickle_list           | 5.34 us                                                    | 5.53 us: 1.03x slower                                                  |
| pickle                  | 11.5 us                                                    | 11.9 us: 1.04x slower                                                  |
| async_tree_cpu_io_mixed | 611 ms                                                     | 638 ms: 1.04x slower                                                   |
| regex_dna               | 221 ms                                                     | 231 ms: 1.04x slower                                                   |
| regex_effbot            | 3.67 ms                                                    | 3.92 ms: 1.07x slower                                                  |
| regex_v8                | 25.1 ms                                                    | 27.2 ms: 1.08x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (24): async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_none_tg, dask, async_tree_io, pylint, pycparser, sympy_expand, async_tree_memoization, logging_simple, telco, json, coroutines, xml_etree_iterparse, asyncio_websockets, typing_runtime_protocols, django_template, pprint_safe_repr, json_dumps, comprehensions, bench_mp_pool, coverage, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x