# Results vs. base

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: f6b4125
- commit date: 2024-07-10
- overall geometric mean: 1.00x faster
- HPT reliability: 86.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 275 ms: 1.01x slower                                                    |
| docutils       | 2.88 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| html5lib       | 65.4 ms                                                               | 63.1 ms: 1.04x faster                                                   |
| tornado_http   | 93.8 ms                                                               | 92.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.9 ms: 1.01x faster                                                   |
| pidigits       | 185 ms                                                                | 186 ms: 1.01x slower                                                    |
| nbody          | 79.5 ms                                                               | 80.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                | 229 ms: 1.01x slower                                                    |
| regex_compile  | 135 ms                                                                | 136 ms: 1.01x slower                                                    |
| regex_v8       | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                   |
| regex_effbot   | 3.84 ms                                                               | 4.02 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 207 us: 1.05x faster                                                    |
| pickle_pure_python   | 296 us                                                                | 292 us: 1.01x faster                                                    |
| tomli_loads          | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                  |
| xml_etree_process    | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 99.0 ms                                                               | 99.4 ms: 1.00x slower                                                   |
| xml_etree_generate   | 81.1 ms                                                               | 81.6 ms: 1.01x slower                                                   |
| json_loads           | 27.5 us                                                               | 27.8 us: 1.01x slower                                                   |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 9.77 ms                                                               | 9.91 ms: 1.01x slower                                                   |
| genshi_xml     | 56.9 ms                                                               | 58.7 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-f6b4125 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| logging_silent           | 108 ns                                                                | 98.0 ns: 1.10x faster                                                   |
| mdp                      | 2.71 sec                                                              | 2.53 sec: 1.07x faster                                                  |
| unpickle_pure_python     | 217 us                                                                | 207 us: 1.05x faster                                                    |
| scimark_monte_carlo      | 60.8 ms                                                               | 58.5 ms: 1.04x faster                                                   |
| html5lib                 | 65.4 ms                                                               | 63.1 ms: 1.04x faster                                                   |
| deepcopy_memo            | 28.4 us                                                               | 27.4 us: 1.04x faster                                                   |
| pprint_safe_repr         | 716 ms                                                                | 697 ms: 1.03x faster                                                    |
| deepcopy_reduce          | 2.76 us                                                               | 2.69 us: 1.03x faster                                                   |
| pprint_pformat           | 1.46 sec                                                              | 1.43 sec: 1.02x faster                                                  |
| logging_simple           | 5.61 us                                                               | 5.49 us: 1.02x faster                                                   |
| logging_format           | 6.16 us                                                               | 6.02 us: 1.02x faster                                                   |
| sqlglot_normalize        | 113 ms                                                                | 111 ms: 1.02x faster                                                    |
| sympy_sum                | 167 ms                                                                | 164 ms: 1.02x faster                                                    |
| richards                 | 41.5 ms                                                               | 40.9 ms: 1.02x faster                                                   |
| pyflate                  | 446 ms                                                                | 439 ms: 1.02x faster                                                    |
| dulwich_log              | 68.0 ms                                                               | 67.0 ms: 1.02x faster                                                   |
| raytrace                 | 271 ms                                                                | 267 ms: 1.01x faster                                                    |
| nqueens                  | 86.2 ms                                                               | 85.1 ms: 1.01x faster                                                   |
| typing_runtime_protocols | 171 us                                                                | 169 us: 1.01x faster                                                    |
| tornado_http             | 93.8 ms                                                               | 92.6 ms: 1.01x faster                                                   |
| pickle_pure_python       | 296 us                                                                | 292 us: 1.01x faster                                                    |
| deepcopy                 | 274 us                                                                | 271 us: 1.01x faster                                                    |
| asyncio_tcp              | 504 ms                                                                | 500 ms: 1.01x faster                                                    |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                  |
| float                    | 70.4 ms                                                               | 69.9 ms: 1.01x faster                                                   |
| sqlglot_optimize         | 55.7 ms                                                               | 55.3 ms: 1.01x faster                                                   |
| sqlglot_parse            | 1.28 ms                                                               | 1.27 ms: 1.01x faster                                                   |
| bench_thread_pool        | 833 us                                                                | 829 us: 1.01x faster                                                    |
| xml_etree_process        | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                   |
| asyncio_websockets       | 558 ms                                                                | 555 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| xml_etree_iterparse      | 99.0 ms                                                               | 99.4 ms: 1.00x slower                                                   |
| sympy_str                | 293 ms                                                                | 295 ms: 1.00x slower                                                    |
| create_gc_cycles         | 1.77 ms                                                               | 1.78 ms: 1.01x slower                                                   |
| sympy_expand             | 493 ms                                                                | 496 ms: 1.01x slower                                                    |
| async_generators         | 455 ms                                                                | 458 ms: 1.01x slower                                                    |
| regex_dna                | 227 ms                                                                | 229 ms: 1.01x slower                                                    |
| pidigits                 | 185 ms                                                                | 186 ms: 1.01x slower                                                    |
| xml_etree_generate       | 81.1 ms                                                               | 81.6 ms: 1.01x slower                                                   |
| nbody                    | 79.5 ms                                                               | 80.0 ms: 1.01x slower                                                   |
| deltablue                | 3.58 ms                                                               | 3.60 ms: 1.01x slower                                                   |
| richards_super           | 47.7 ms                                                               | 48.0 ms: 1.01x slower                                                   |
| docutils                 | 2.88 sec                                                              | 2.90 sec: 1.01x slower                                                  |
| regex_compile            | 135 ms                                                                | 136 ms: 1.01x slower                                                    |
| regex_v8                 | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                   |
| json_loads               | 27.5 us                                                               | 27.8 us: 1.01x slower                                                   |
| telco                    | 7.92 ms                                                               | 8.00 ms: 1.01x slower                                                   |
| 2to3                     | 272 ms                                                                | 275 ms: 1.01x slower                                                    |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                   |
| hexiom                   | 6.56 ms                                                               | 6.65 ms: 1.01x slower                                                   |
| mako                     | 9.77 ms                                                               | 9.91 ms: 1.01x slower                                                   |
| pathlib                  | 15.9 ms                                                               | 16.2 ms: 1.02x slower                                                   |
| genshi_xml               | 56.9 ms                                                               | 58.7 ms: 1.03x slower                                                   |
| spectral_norm            | 101 ms                                                                | 105 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.53 ms: 1.03x slower                                                   |
| gc_traversal             | 3.64 ms                                                               | 3.78 ms: 1.04x slower                                                   |
| regex_effbot             | 3.84 ms                                                               | 4.02 ms: 1.05x slower                                                   |
| scimark_fft              | 305 ms                                                                | 320 ms: 1.05x slower                                                    |
| chaos                    | 57.8 ms                                                               | 61.7 ms: 1.07x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (30): xml_etree_parse, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, scimark_sor, fannkuch, async_tree_none, meteor_contest, coverage, async_tree_cpu_io_mixed, django_template, async_tree_none_tg, async_tree_io_tg, bpe_tokeniser, sqlglot_transpile, go, coroutines, async_tree_memoization, bench_mp_pool, crypto_pyaes, dask, comprehensions, sympy_integrate, thrift, generators, json, pycparser, scimark_lu, genshi_text, async_tree_io, pylint

# HPT report

- Reliability score: 86.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x