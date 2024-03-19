# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.00x faster
- HPT reliability: 55.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                                               | 2.78 sec: 1.00x slower                                                       |
| html5lib       | 67.7 ms                                                                | 66.4 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg | 459 ms                                                                 | 458 ms: 1.00x faster                                                         |
| async_tree_io      | 1.21 sec                                                               | 1.22 sec: 1.01x slower                                                       |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 189 ms: 1.00x faster                                                         |
| float          | 80.1 ms                                                                | 80.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                                | 25.8 ms: 1.00x slower                                                        |
| regex_dna      | 228 ms                                                                 | 231 ms: 1.01x slower                                                         |
| regex_effbot   | 3.76 ms                                                                | 3.85 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list       | 5.12 us                                                                | 5.02 us: 1.02x faster                                                        |
| pickle_dict         | 34.5 us                                                                | 34.1 us: 1.01x faster                                                        |
| pickle_list         | 4.96 us                                                                | 4.92 us: 1.01x faster                                                        |
| xml_etree_process   | 60.2 ms                                                                | 59.9 ms: 1.01x faster                                                        |
| json_dumps          | 10.5 ms                                                                | 10.4 ms: 1.00x faster                                                        |
| pickle              | 11.5 us                                                                | 11.6 us: 1.01x slower                                                        |
| xml_etree_iterparse | 107 ms                                                                 | 108 ms: 1.01x slower                                                         |
| pickle_pure_python  | 298 us                                                                 | 302 us: 1.01x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): unpickle, tomli_loads, xml_etree_generate, json_loads, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 11.2 ms                                                                | 10.3 ms: 1.08x faster                                                        |
| python_startup         | 12.6 ms                                                                | 11.8 ms: 1.07x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 24.1 ms                                                                | 24.3 ms: 1.01x slower                                                        |
| mako            | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                        |
| django_template | 34.3 ms                                                                | 34.9 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240313-linux-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| bench_mp_pool          | 26.4 ms                                                                | 24.0 ms: 1.10x faster                                                        |
| python_startup_no_site | 11.2 ms                                                                | 10.3 ms: 1.08x faster                                                        |
| python_startup         | 12.6 ms                                                                | 11.8 ms: 1.07x faster                                                        |
| logging_silent         | 104 ns                                                                 | 101 ns: 1.03x faster                                                         |
| unpickle_list          | 5.12 us                                                                | 5.02 us: 1.02x faster                                                        |
| html5lib               | 67.7 ms                                                                | 66.4 ms: 1.02x faster                                                        |
| async_generators       | 472 ms                                                                 | 464 ms: 1.02x faster                                                         |
| coroutines             | 23.3 ms                                                                | 22.9 ms: 1.02x faster                                                        |
| scimark_sor            | 130 ms                                                                 | 128 ms: 1.01x faster                                                         |
| nqueens                | 90.3 ms                                                                | 89.3 ms: 1.01x faster                                                        |
| pickle_dict            | 34.5 us                                                                | 34.1 us: 1.01x faster                                                        |
| scimark_lu             | 131 ms                                                                 | 129 ms: 1.01x faster                                                         |
| telco                  | 8.41 ms                                                                | 8.33 ms: 1.01x faster                                                        |
| pathlib                | 18.8 ms                                                                | 18.7 ms: 1.01x faster                                                        |
| coverage               | 97.7 ms                                                                | 96.9 ms: 1.01x faster                                                        |
| pickle_list            | 4.96 us                                                                | 4.92 us: 1.01x faster                                                        |
| raytrace               | 297 ms                                                                 | 295 ms: 1.01x faster                                                         |
| sympy_str              | 287 ms                                                                 | 285 ms: 1.01x faster                                                         |
| deepcopy_memo          | 39.1 us                                                                | 38.9 us: 1.01x faster                                                        |
| xml_etree_process      | 60.2 ms                                                                | 59.9 ms: 1.01x faster                                                        |
| comprehensions         | 17.4 us                                                                | 17.3 us: 1.01x faster                                                        |
| sqlglot_optimize       | 56.6 ms                                                                | 56.3 ms: 1.01x faster                                                        |
| pidigits               | 190 ms                                                                 | 189 ms: 1.00x faster                                                         |
| dulwich_log            | 70.8 ms                                                                | 70.5 ms: 1.00x faster                                                        |
| json_dumps             | 10.5 ms                                                                | 10.4 ms: 1.00x faster                                                        |
| sympy_integrate        | 21.3 ms                                                                | 21.2 ms: 1.00x faster                                                        |
| bench_thread_pool      | 862 us                                                                 | 859 us: 1.00x faster                                                         |
| fannkuch               | 398 ms                                                                 | 397 ms: 1.00x faster                                                         |
| sqlglot_normalize      | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| async_tree_none_tg     | 459 ms                                                                 | 458 ms: 1.00x faster                                                         |
| scimark_fft            | 339 ms                                                                 | 340 ms: 1.00x slower                                                         |
| go                     | 158 ms                                                                 | 158 ms: 1.00x slower                                                         |
| hexiom                 | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                                        |
| regex_v8               | 25.7 ms                                                                | 25.8 ms: 1.00x slower                                                        |
| asyncio_tcp            | 502 ms                                                                 | 504 ms: 1.00x slower                                                         |
| generators             | 29.6 ms                                                                | 29.8 ms: 1.00x slower                                                        |
| docutils               | 2.77 sec                                                               | 2.78 sec: 1.00x slower                                                       |
| float                  | 80.1 ms                                                                | 80.5 ms: 1.01x slower                                                        |
| mdp                    | 2.82 sec                                                               | 2.84 sec: 1.01x slower                                                       |
| async_tree_io          | 1.21 sec                                                               | 1.22 sec: 1.01x slower                                                       |
| pickle                 | 11.5 us                                                                | 11.6 us: 1.01x slower                                                        |
| xml_etree_iterparse    | 107 ms                                                                 | 108 ms: 1.01x slower                                                         |
| genshi_text            | 24.1 ms                                                                | 24.3 ms: 1.01x slower                                                        |
| mako                   | 10.9 ms                                                                | 11.0 ms: 1.01x slower                                                        |
| thrift                 | 793 us                                                                 | 802 us: 1.01x slower                                                         |
| scimark_monte_carlo    | 70.2 ms                                                                | 71.0 ms: 1.01x slower                                                        |
| richards_super         | 52.4 ms                                                                | 53.0 ms: 1.01x slower                                                        |
| richards               | 46.1 ms                                                                | 46.7 ms: 1.01x slower                                                        |
| logging_simple         | 5.81 us                                                                | 5.88 us: 1.01x slower                                                        |
| pickle_pure_python     | 298 us                                                                 | 302 us: 1.01x slower                                                         |
| regex_dna              | 228 ms                                                                 | 231 ms: 1.01x slower                                                         |
| create_gc_cycles       | 1.52 ms                                                                | 1.55 ms: 1.02x slower                                                        |
| django_template        | 34.3 ms                                                                | 34.9 ms: 1.02x slower                                                        |
| pprint_safe_repr       | 756 ms                                                                 | 772 ms: 1.02x slower                                                         |
| regex_effbot           | 3.76 ms                                                                | 3.85 ms: 1.02x slower                                                        |
| unpack_sequence        | 86.4 ns                                                                | 89.2 ns: 1.03x slower                                                        |
| gc_traversal           | 3.58 ms                                                                | 3.92 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (45): async_tree_memoization_tg, json, unpickle, sqlglot_parse, mypy2, deepcopy_reduce, tomli_loads, regex_compile, async_tree_cpu_io_mixed, sympy_sum, nbody, deltablue, 2to3, asyncio_websockets, chaos, gunicorn, xml_etree_generate, deepcopy, aiohttp, typing_runtime_protocols, sqlglot_transpile, chameleon, crypto_pyaes, dask, tornado_http, meteor_contest, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, pycparser, sympy_expand, json_loads, async_tree_io_tg, scimark_sparse_mat_mult, unpickle_pure_python, spectral_norm, pyflate, async_tree_none, pylint, xml_etree_parse, djangocms, logging_format, sqlite_synth, genshi_xml, pprint_pformat


# HPT report

- Reliability score: 55.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x