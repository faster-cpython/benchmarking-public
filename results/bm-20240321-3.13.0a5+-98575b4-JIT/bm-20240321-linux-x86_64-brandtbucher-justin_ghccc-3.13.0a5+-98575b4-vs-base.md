# Results vs. base

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.01x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                 | 303 ms: 1.01x faster                                                 |
| html5lib       | 76.3 ms                                                                | 75.2 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg | 3.76 sec                                                               | 3.75 sec: 1.00x faster                                               |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 92.7 ms                                                                | 81.4 ms: 1.14x faster                                                |
| float          | 143 ms                                                                 | 139 ms: 1.03x faster                                                 |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.90 ms                                                                | 3.70 ms: 1.06x faster                                                |
| regex_dna      | 234 ms                                                                 | 227 ms: 1.03x faster                                                 |
| regex_compile  | 143 ms                                                                 | 142 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.13 sec                                                               | 2.00 sec: 1.07x faster                                               |
| unpickle_pure_python | 238 us                                                                 | 227 us: 1.05x faster                                                 |
| unpickle_list        | 5.40 us                                                                | 5.17 us: 1.05x faster                                                |
| xml_etree_iterparse  | 164 ms                                                                 | 162 ms: 1.01x faster                                                 |
| pickle_list          | 5.24 us                                                                | 5.20 us: 1.01x faster                                                |
| json_loads           | 28.5 us                                                                | 28.4 us: 1.01x faster                                                |
| unpickle             | 15.2 us                                                                | 15.1 us: 1.00x faster                                                |
| pickle_dict          | 34.7 us                                                                | 36.3 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (6): xml_etree_generate, pickle_pure_python, xml_etree_process, pickle, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.9 ms                                                                | 10.4 ms: 1.05x faster                                                |
| genshi_xml      | 61.0 ms                                                                | 60.5 ms: 1.01x faster                                                |
| genshi_text     | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| django_template | 34.6 ms                                                                | 35.5 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240320-linux-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| spectral_norm            | 115 ms                                                                 | 100 ms: 1.15x faster                                                 |
| nbody                    | 92.7 ms                                                                | 81.4 ms: 1.14x faster                                                |
| crypto_pyaes             | 76.6 ms                                                                | 69.0 ms: 1.11x faster                                                |
| fannkuch                 | 411 ms                                                                 | 373 ms: 1.10x faster                                                 |
| scimark_fft              | 345 ms                                                                 | 316 ms: 1.09x faster                                                 |
| scimark_monte_carlo      | 71.3 ms                                                                | 65.2 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult  | 4.99 ms                                                                | 4.61 ms: 1.08x faster                                                |
| pyflate                  | 490 ms                                                                 | 456 ms: 1.07x faster                                                 |
| tomli_loads              | 2.13 sec                                                               | 2.00 sec: 1.07x faster                                               |
| richards                 | 47.5 ms                                                                | 45.0 ms: 1.06x faster                                                |
| regex_effbot             | 3.90 ms                                                                | 3.70 ms: 1.06x faster                                                |
| raytrace                 | 298 ms                                                                 | 283 ms: 1.05x faster                                                 |
| mako                     | 10.9 ms                                                                | 10.4 ms: 1.05x faster                                                |
| chaos                    | 64.6 ms                                                                | 61.6 ms: 1.05x faster                                                |
| unpickle_pure_python     | 238 us                                                                 | 227 us: 1.05x faster                                                 |
| pprint_safe_repr         | 760 ms                                                                 | 726 ms: 1.05x faster                                                 |
| unpickle_list            | 5.40 us                                                                | 5.17 us: 1.05x faster                                                |
| pprint_pformat           | 1.57 sec                                                               | 1.50 sec: 1.04x faster                                               |
| comprehensions           | 17.6 us                                                                | 16.9 us: 1.04x faster                                                |
| scimark_lu               | 132 ms                                                                 | 127 ms: 1.04x faster                                                 |
| hexiom                   | 7.02 ms                                                                | 6.79 ms: 1.03x faster                                                |
| nqueens                  | 92.3 ms                                                                | 89.4 ms: 1.03x faster                                                |
| regex_dna                | 234 ms                                                                 | 227 ms: 1.03x faster                                                 |
| richards_super           | 53.2 ms                                                                | 51.7 ms: 1.03x faster                                                |
| float                    | 143 ms                                                                 | 139 ms: 1.03x faster                                                 |
| pathlib                  | 19.3 ms                                                                | 18.8 ms: 1.03x faster                                                |
| logging_format           | 6.66 us                                                                | 6.49 us: 1.03x faster                                                |
| typing_runtime_protocols | 115 us                                                                 | 113 us: 1.02x faster                                                 |
| sqlite_synth             | 2.89 us                                                                | 2.83 us: 1.02x faster                                                |
| telco                    | 8.65 ms                                                                | 8.50 ms: 1.02x faster                                                |
| logging_simple           | 5.95 us                                                                | 5.84 us: 1.02x faster                                                |
| html5lib                 | 76.3 ms                                                                | 75.2 ms: 1.01x faster                                                |
| deepcopy_reduce          | 3.17 us                                                                | 3.12 us: 1.01x faster                                                |
| xml_etree_iterparse      | 164 ms                                                                 | 162 ms: 1.01x faster                                                 |
| deepcopy_memo            | 39.0 us                                                                | 38.6 us: 1.01x faster                                                |
| 2to3                     | 306 ms                                                                 | 303 ms: 1.01x faster                                                 |
| deepcopy                 | 358 us                                                                 | 354 us: 1.01x faster                                                 |
| sympy_str                | 288 ms                                                                 | 286 ms: 1.01x faster                                                 |
| regex_compile            | 143 ms                                                                 | 142 ms: 1.01x faster                                                 |
| json                     | 5.27 ms                                                                | 5.22 ms: 1.01x faster                                                |
| pickle_list              | 5.24 us                                                                | 5.20 us: 1.01x faster                                                |
| sympy_sum                | 163 ms                                                                 | 162 ms: 1.01x faster                                                 |
| genshi_xml               | 61.0 ms                                                                | 60.5 ms: 1.01x faster                                                |
| meteor_contest           | 110 ms                                                                 | 109 ms: 1.01x faster                                                 |
| sympy_integrate          | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                                |
| json_loads               | 28.5 us                                                                | 28.4 us: 1.01x faster                                                |
| sympy_expand             | 490 ms                                                                 | 487 ms: 1.01x faster                                                 |
| unpickle                 | 15.2 us                                                                | 15.1 us: 1.00x faster                                                |
| async_tree_none_tg       | 3.76 sec                                                               | 3.75 sec: 1.00x faster                                               |
| python_startup           | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                                |
| pidigits                 | 189 ms                                                                 | 189 ms: 1.00x faster                                                 |
| bench_thread_pool        | 858 us                                                                 | 856 us: 1.00x faster                                                 |
| async_generators         | 555 ms                                                                 | 557 ms: 1.01x slower                                                 |
| asyncio_tcp              | 506 ms                                                                 | 510 ms: 1.01x slower                                                 |
| coroutines               | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                |
| dulwich_log              | 70.1 ms                                                                | 71.0 ms: 1.01x slower                                                |
| genshi_text              | 24.6 ms                                                                | 25.1 ms: 1.02x slower                                                |
| scimark_sor              | 129 ms                                                                 | 132 ms: 1.02x slower                                                 |
| django_template          | 34.6 ms                                                                | 35.5 ms: 1.02x slower                                                |
| pickle_dict              | 34.7 us                                                                | 36.3 us: 1.05x slower                                                |
| gc_traversal             | 3.45 ms                                                                | 3.75 ms: 1.09x slower                                                |
| unpack_sequence          | 86.8 ns                                                                | 113 ns: 1.30x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (40): logging_silent, sqlglot_transpile, djangocms, deltablue, async_tree_io_tg, pycparser, bench_mp_pool, asyncio_websockets, sqlglot_optimize, gunicorn, xml_etree_generate, sqlglot_normalize, create_gc_cycles, generators, aiohttp, thrift, python_startup_no_site, pickle_pure_python, xml_etree_process, async_tree_io, async_tree_memoization, docutils, mdp, go, asyncio_tcp_ssl, chameleon, pickle, tornado_http, regex_v8, async_tree_none, sqlglot_parse, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, json_dumps, async_tree_cpu_io_mixed, dask, mypy2, xml_etree_parse, pylint, coverage


# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x