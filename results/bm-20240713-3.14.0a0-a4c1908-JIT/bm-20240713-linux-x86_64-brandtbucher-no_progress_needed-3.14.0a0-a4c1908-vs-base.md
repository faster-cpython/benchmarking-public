# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 68.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 275 ms: 1.01x slower                                                      |
| docutils       | 2.88 sec                                                              | 2.92 sec: 1.01x slower                                                    |
| html5lib       | 65.4 ms                                                               | 63.6 ms: 1.03x faster                                                     |
| tornado_http   | 93.8 ms                                                               | 92.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| nbody          | 79.5 ms                                                               | 80.5 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.84 ms                                                               | 3.75 ms: 1.02x faster                                                     |
| regex_v8       | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                     |
| regex_dna      | 227 ms                                                                | 228 ms: 1.00x slower                                                      |
| regex_compile  | 135 ms                                                                | 137 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.87 sec: 1.03x faster                                                    |
| unpickle_pure_python | 217 us                                                                | 213 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                                     |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| xml_etree_generate   | 81.1 ms                                                               | 81.9 ms: 1.01x slower                                                     |
| pickle_pure_python   | 296 us                                                                | 308 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 34.9 ms: 1.03x faster                                                     |
| mako            | 9.77 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| genshi_text     | 25.1 ms                                                               | 25.9 ms: 1.03x slower                                                     |
| genshi_xml      | 56.9 ms                                                               | 58.7 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards_super           | 47.7 ms                                                               | 40.8 ms: 1.17x faster                                                     |
| richards                 | 41.5 ms                                                               | 35.9 ms: 1.16x faster                                                     |
| mdp                      | 2.71 sec                                                              | 2.54 sec: 1.07x faster                                                    |
| logging_silent           | 108 ns                                                                | 101 ns: 1.07x faster                                                      |
| scimark_lu               | 126 ms                                                                | 119 ms: 1.06x faster                                                      |
| deepcopy_memo            | 28.4 us                                                               | 27.1 us: 1.05x faster                                                     |
| dulwich_log              | 68.0 ms                                                               | 65.2 ms: 1.04x faster                                                     |
| deltablue                | 3.58 ms                                                               | 3.45 ms: 1.04x faster                                                     |
| deepcopy                 | 274 us                                                                | 265 us: 1.03x faster                                                      |
| django_template          | 36.1 ms                                                               | 34.9 ms: 1.03x faster                                                     |
| tomli_loads              | 1.93 sec                                                              | 1.87 sec: 1.03x faster                                                    |
| logging_simple           | 5.61 us                                                               | 5.45 us: 1.03x faster                                                     |
| html5lib                 | 65.4 ms                                                               | 63.6 ms: 1.03x faster                                                     |
| deepcopy_reduce          | 2.76 us                                                               | 2.68 us: 1.03x faster                                                     |
| scimark_sor              | 131 ms                                                                | 128 ms: 1.03x faster                                                      |
| regex_effbot             | 3.84 ms                                                               | 3.75 ms: 1.02x faster                                                     |
| pyflate                  | 446 ms                                                                | 437 ms: 1.02x faster                                                      |
| bpe_tokeniser            | 4.82 sec                                                              | 4.72 sec: 1.02x faster                                                    |
| logging_format           | 6.16 us                                                               | 6.04 us: 1.02x faster                                                     |
| tornado_http             | 93.8 ms                                                               | 92.2 ms: 1.02x faster                                                     |
| unpickle_pure_python     | 217 us                                                                | 213 us: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.31 ms: 1.02x faster                                                     |
| sympy_str                | 293 ms                                                                | 289 ms: 1.02x faster                                                      |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.01x faster                                                      |
| float                    | 70.4 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| coroutines               | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                                     |
| meteor_contest           | 108 ms                                                                | 107 ms: 1.01x faster                                                      |
| typing_runtime_protocols | 171 us                                                                | 169 us: 1.01x faster                                                      |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                                      |
| sympy_integrate          | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                     |
| bench_thread_pool        | 833 us                                                                | 827 us: 1.01x faster                                                      |
| sympy_sum                | 167 ms                                                                | 166 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 99.0 ms                                                               | 98.4 ms: 1.01x faster                                                     |
| async_generators         | 455 ms                                                                | 452 ms: 1.01x faster                                                      |
| crypto_pyaes             | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                                     |
| telco                    | 7.92 ms                                                               | 7.88 ms: 1.01x faster                                                     |
| asyncio_websockets       | 558 ms                                                                | 555 ms: 1.00x faster                                                      |
| regex_v8                 | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                     |
| python_startup_no_site   | 7.11 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| regex_dna                | 227 ms                                                                | 228 ms: 1.00x slower                                                      |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                      |
| asyncio_tcp              | 504 ms                                                                | 507 ms: 1.00x slower                                                      |
| raytrace                 | 271 ms                                                                | 273 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.77 ms                                                               | 1.78 ms: 1.01x slower                                                     |
| pathlib                  | 15.9 ms                                                               | 16.0 ms: 1.01x slower                                                     |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                     |
| sqlglot_optimize         | 55.7 ms                                                               | 56.2 ms: 1.01x slower                                                     |
| xml_etree_generate       | 81.1 ms                                                               | 81.9 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                     |
| docutils                 | 2.88 sec                                                              | 2.92 sec: 1.01x slower                                                    |
| 2to3                     | 272 ms                                                                | 275 ms: 1.01x slower                                                      |
| nbody                    | 79.5 ms                                                               | 80.5 ms: 1.01x slower                                                     |
| regex_compile            | 135 ms                                                                | 137 ms: 1.01x slower                                                      |
| thrift                   | 799 us                                                                | 812 us: 1.02x slower                                                      |
| scimark_fft              | 305 ms                                                                | 311 ms: 1.02x slower                                                      |
| spectral_norm            | 101 ms                                                                | 104 ms: 1.02x slower                                                      |
| sqlglot_transpile        | 1.60 ms                                                               | 1.64 ms: 1.02x slower                                                     |
| hexiom                   | 6.56 ms                                                               | 6.73 ms: 1.03x slower                                                     |
| mako                     | 9.77 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| scimark_monte_carlo      | 60.8 ms                                                               | 62.4 ms: 1.03x slower                                                     |
| genshi_text              | 25.1 ms                                                               | 25.9 ms: 1.03x slower                                                     |
| genshi_xml               | 56.9 ms                                                               | 58.7 ms: 1.03x slower                                                     |
| pprint_safe_repr         | 716 ms                                                                | 740 ms: 1.03x slower                                                      |
| pickle_pure_python       | 296 us                                                                | 308 us: 1.04x slower                                                      |
| pprint_pformat           | 1.46 sec                                                              | 1.53 sec: 1.04x slower                                                    |
| gc_traversal             | 3.64 ms                                                               | 3.85 ms: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (24): fannkuch, coverage, dask, async_tree_io_tg, xml_etree_parse, chaos, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, comprehensions, bench_mp_pool, asyncio_tcp_ssl, async_tree_none_tg, json_loads, sympy_expand, generators, xml_etree_process, async_tree_none, nqueens, async_tree_io, json, async_tree_cpu_io_mixed, pycparser, async_tree_memoization, pylint

# HPT report

- Reliability score: 68.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x