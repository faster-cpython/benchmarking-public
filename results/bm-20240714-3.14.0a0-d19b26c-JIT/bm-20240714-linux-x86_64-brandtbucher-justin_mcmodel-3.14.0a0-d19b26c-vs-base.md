# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.00x faster
- HPT reliability: 98.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                | 268 ms: 1.01x faster                                                  |
| docutils       | 2.84 sec                                                              | 2.83 sec: 1.00x faster                                                |
| html5lib       | 64.8 ms                                                               | 65.4 ms: 1.01x slower                                                 |
| tornado_http   | 93.5 ms                                                               | 92.1 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 79.9 ms                                                               | 75.6 ms: 1.06x faster                                                 |
| float          | 70.0 ms                                                               | 69.7 ms: 1.00x faster                                                 |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 132 ms: 1.01x faster                                                  |
| regex_v8       | 23.9 ms                                                               | 24.5 ms: 1.03x slower                                                 |
| regex_dna      | 224 ms                                                                | 230 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.97 sec                                                              | 1.92 sec: 1.03x faster                                                |
| xml_etree_iterparse  | 98.7 ms                                                               | 99.0 ms: 1.00x slower                                                 |
| xml_etree_generate   | 81.3 ms                                                               | 81.7 ms: 1.00x slower                                                 |
| json_loads           | 27.6 us                                                               | 27.7 us: 1.00x slower                                                 |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                 |
| xml_etree_process    | 57.2 ms                                                               | 57.7 ms: 1.01x slower                                                 |
| unpickle_pure_python | 215 us                                                                | 217 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                               | 7.12 ms: 1.01x slower                                                 |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 24.8 ms                                                               | 23.8 ms: 1.04x faster                                                 |
| genshi_xml      | 57.8 ms                                                               | 55.6 ms: 1.04x faster                                                 |
| mako            | 9.76 ms                                                               | 9.73 ms: 1.00x faster                                                 |
| django_template | 35.6 ms                                                               | 35.8 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody                    | 79.9 ms                                                               | 75.6 ms: 1.06x faster                                                 |
| genshi_text              | 24.8 ms                                                               | 23.8 ms: 1.04x faster                                                 |
| richards_super           | 47.7 ms                                                               | 45.8 ms: 1.04x faster                                                 |
| genshi_xml               | 57.8 ms                                                               | 55.6 ms: 1.04x faster                                                 |
| richards                 | 42.1 ms                                                               | 40.5 ms: 1.04x faster                                                 |
| logging_simple           | 5.62 us                                                               | 5.42 us: 1.04x faster                                                 |
| logging_format           | 6.19 us                                                               | 5.99 us: 1.03x faster                                                 |
| tomli_loads              | 1.97 sec                                                              | 1.92 sec: 1.03x faster                                                |
| comprehensions           | 16.9 us                                                               | 16.5 us: 1.02x faster                                                 |
| deepcopy_memo            | 28.5 us                                                               | 27.9 us: 1.02x faster                                                 |
| go                       | 144 ms                                                                | 141 ms: 1.02x faster                                                  |
| pycparser                | 1.14 sec                                                              | 1.12 sec: 1.02x faster                                                |
| hexiom                   | 6.57 ms                                                               | 6.45 ms: 1.02x faster                                                 |
| pyflate                  | 436 ms                                                                | 429 ms: 1.02x faster                                                  |
| deltablue                | 3.61 ms                                                               | 3.55 ms: 1.02x faster                                                 |
| tornado_http             | 93.5 ms                                                               | 92.1 ms: 1.02x faster                                                 |
| coroutines               | 23.6 ms                                                               | 23.3 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 1.59 ms                                                               | 1.57 ms: 1.01x faster                                                 |
| deepcopy_reduce          | 2.78 us                                                               | 2.75 us: 1.01x faster                                                 |
| regex_compile            | 134 ms                                                                | 132 ms: 1.01x faster                                                  |
| sqlglot_parse            | 1.27 ms                                                               | 1.26 ms: 1.01x faster                                                 |
| sympy_sum                | 165 ms                                                                | 163 ms: 1.01x faster                                                  |
| sympy_str                | 292 ms                                                                | 289 ms: 1.01x faster                                                  |
| crypto_pyaes             | 67.5 ms                                                               | 66.8 ms: 1.01x faster                                                 |
| asyncio_tcp              | 506 ms                                                                | 501 ms: 1.01x faster                                                  |
| sympy_integrate          | 21.8 ms                                                               | 21.7 ms: 1.01x faster                                                 |
| 2to3                     | 270 ms                                                                | 268 ms: 1.01x faster                                                  |
| sympy_expand             | 491 ms                                                                | 488 ms: 1.01x faster                                                  |
| async_generators         | 457 ms                                                                | 455 ms: 1.00x faster                                                  |
| float                    | 70.0 ms                                                               | 69.7 ms: 1.00x faster                                                 |
| docutils                 | 2.84 sec                                                              | 2.83 sec: 1.00x faster                                                |
| bench_thread_pool        | 837 us                                                                | 834 us: 1.00x faster                                                  |
| dulwich_log              | 67.5 ms                                                               | 67.3 ms: 1.00x faster                                                 |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.00x faster                                                  |
| generators               | 29.8 ms                                                               | 29.7 ms: 1.00x faster                                                 |
| mako                     | 9.76 ms                                                               | 9.73 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| xml_etree_iterparse      | 98.7 ms                                                               | 99.0 ms: 1.00x slower                                                 |
| xml_etree_generate       | 81.3 ms                                                               | 81.7 ms: 1.00x slower                                                 |
| json_loads               | 27.6 us                                                               | 27.7 us: 1.00x slower                                                 |
| sqlglot_normalize        | 111 ms                                                                | 111 ms: 1.01x slower                                                  |
| coverage                 | 92.0 ms                                                               | 92.5 ms: 1.01x slower                                                 |
| python_startup_no_site   | 7.08 ms                                                               | 7.12 ms: 1.01x slower                                                 |
| mdp                      | 2.54 sec                                                              | 2.56 sec: 1.01x slower                                                |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                 |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                 |
| django_template          | 35.6 ms                                                               | 35.8 ms: 1.01x slower                                                 |
| scimark_lu               | 125 ms                                                                | 126 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 60.1 ms                                                               | 60.6 ms: 1.01x slower                                                 |
| xml_etree_process        | 57.2 ms                                                               | 57.7 ms: 1.01x slower                                                 |
| html5lib                 | 64.8 ms                                                               | 65.4 ms: 1.01x slower                                                 |
| unpickle_pure_python     | 215 us                                                                | 217 us: 1.01x slower                                                  |
| pprint_pformat           | 1.44 sec                                                              | 1.46 sec: 1.01x slower                                                |
| scimark_fft              | 312 ms                                                                | 316 ms: 1.01x slower                                                  |
| create_gc_cycles         | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 166 us                                                                | 169 us: 1.02x slower                                                  |
| bpe_tokeniser            | 4.75 sec                                                              | 4.84 sec: 1.02x slower                                                |
| regex_v8                 | 23.9 ms                                                               | 24.5 ms: 1.03x slower                                                 |
| regex_dna                | 224 ms                                                                | 230 ms: 1.03x slower                                                  |
| telco                    | 7.96 ms                                                               | 8.23 ms: 1.03x slower                                                 |
| fannkuch                 | 358 ms                                                                | 380 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.57 ms: 1.09x slower                                                 |
| gc_traversal             | 3.52 ms                                                               | 3.88 ms: 1.10x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (27): pylint, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, dask, async_tree_cpu_io_mixed_tg, pathlib, deepcopy, async_tree_memoization_tg, logging_silent, pickle_pure_python, json, scimark_sor, sqlglot_optimize, async_tree_none_tg, spectral_norm, bench_mp_pool, chaos, thrift, asyncio_websockets, async_tree_io, raytrace, async_tree_io_tg, regex_effbot, pprint_safe_repr, nqueens, xml_etree_parse

# HPT report

- Reliability score: 98.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x