# Results vs. base

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.00x faster
- HPT reliability: 99.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 271 ms: 1.00x faster                                                    |
| docutils       | 2.88 sec                                                              | 2.85 sec: 1.01x faster                                                  |
| html5lib       | 65.4 ms                                                               | 63.0 ms: 1.04x faster                                                   |
| tornado_http   | 93.8 ms                                                               | 92.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.84 ms                                                               | 3.75 ms: 1.02x faster                                                   |
| regex_v8       | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                                   |
| unpickle_pure_python | 217 us                                                                | 216 us: 1.00x faster                                                    |
| tomli_loads          | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                  |
| json_loads           | 27.5 us                                                               | 27.9 us: 1.01x slower                                                   |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 35.3 ms: 1.02x faster                                                   |
| genshi_text     | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                                   |
| mako            | 9.77 ms                                                               | 9.84 ms: 1.01x slower                                                   |
| genshi_xml      | 56.9 ms                                                               | 58.1 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                      | 2.71 sec                                                              | 2.56 sec: 1.06x faster                                                  |
| html5lib                 | 65.4 ms                                                               | 63.0 ms: 1.04x faster                                                   |
| sqlglot_normalize        | 113 ms                                                                | 110 ms: 1.03x faster                                                    |
| logging_simple           | 5.61 us                                                               | 5.48 us: 1.02x faster                                                   |
| regex_effbot             | 3.84 ms                                                               | 3.75 ms: 1.02x faster                                                   |
| django_template          | 36.1 ms                                                               | 35.3 ms: 1.02x faster                                                   |
| scimark_lu               | 126 ms                                                                | 123 ms: 1.02x faster                                                    |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.02x faster                                                    |
| sympy_sum                | 167 ms                                                                | 165 ms: 1.01x faster                                                    |
| tornado_http             | 93.8 ms                                                               | 92.5 ms: 1.01x faster                                                   |
| deepcopy_reduce          | 2.76 us                                                               | 2.72 us: 1.01x faster                                                   |
| sqlglot_parse            | 1.28 ms                                                               | 1.26 ms: 1.01x faster                                                   |
| docutils                 | 2.88 sec                                                              | 2.85 sec: 1.01x faster                                                  |
| genshi_text              | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                                   |
| sqlglot_transpile        | 1.60 ms                                                               | 1.58 ms: 1.01x faster                                                   |
| thrift                   | 799 us                                                                | 792 us: 1.01x faster                                                    |
| dulwich_log              | 68.0 ms                                                               | 67.4 ms: 1.01x faster                                                   |
| float                    | 70.4 ms                                                               | 69.8 ms: 1.01x faster                                                   |
| deltablue                | 3.58 ms                                                               | 3.55 ms: 1.01x faster                                                   |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                                    |
| logging_format           | 6.16 us                                                               | 6.11 us: 1.01x faster                                                   |
| hexiom                   | 6.56 ms                                                               | 6.52 ms: 1.01x faster                                                   |
| generators               | 29.8 ms                                                               | 29.6 ms: 1.01x faster                                                   |
| sqlglot_optimize         | 55.7 ms                                                               | 55.4 ms: 1.01x faster                                                   |
| xml_etree_iterparse      | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                                   |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.01x faster                                                   |
| deepcopy_memo            | 28.4 us                                                               | 28.2 us: 1.01x faster                                                   |
| unpickle_pure_python     | 217 us                                                                | 216 us: 1.00x faster                                                    |
| 2to3                     | 272 ms                                                                | 271 ms: 1.00x faster                                                    |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.36 ms: 1.00x faster                                                   |
| regex_v8                 | 25.5 ms                                                               | 25.4 ms: 1.00x faster                                                   |
| python_startup_no_site   | 7.11 ms                                                               | 7.10 ms: 1.00x faster                                                   |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                   |
| bench_thread_pool        | 833 us                                                                | 832 us: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| gc_traversal             | 3.64 ms                                                               | 3.65 ms: 1.00x slower                                                   |
| sympy_expand             | 493 ms                                                                | 495 ms: 1.00x slower                                                    |
| coroutines               | 23.5 ms                                                               | 23.6 ms: 1.00x slower                                                   |
| mako                     | 9.77 ms                                                               | 9.84 ms: 1.01x slower                                                   |
| tomli_loads              | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                  |
| scimark_sor              | 131 ms                                                                | 132 ms: 1.01x slower                                                    |
| json_loads               | 27.5 us                                                               | 27.9 us: 1.01x slower                                                   |
| deepcopy                 | 274 us                                                                | 278 us: 1.01x slower                                                    |
| scimark_monte_carlo      | 60.8 ms                                                               | 61.7 ms: 1.02x slower                                                   |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                   |
| telco                    | 7.92 ms                                                               | 8.06 ms: 1.02x slower                                                   |
| scimark_fft              | 305 ms                                                                | 311 ms: 1.02x slower                                                    |
| async_generators         | 455 ms                                                                | 464 ms: 1.02x slower                                                    |
| pathlib                  | 15.9 ms                                                               | 16.3 ms: 1.02x slower                                                   |
| genshi_xml               | 56.9 ms                                                               | 58.1 ms: 1.02x slower                                                   |
| richards_super           | 47.7 ms                                                               | 48.7 ms: 1.02x slower                                                   |
| richards                 | 41.5 ms                                                               | 42.6 ms: 1.03x slower                                                   |
| spectral_norm            | 101 ms                                                                | 106 ms: 1.05x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (38): logging_silent, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, nqueens, crypto_pyaes, comprehensions, raytrace, pickle_pure_python, pycparser, dask, xml_etree_generate, bpe_tokeniser, sympy_str, asyncio_tcp, fannkuch, sympy_integrate, pylint, asyncio_websockets, pidigits, bench_mp_pool, regex_dna, pprint_safe_repr, nbody, json, pyflate, xml_etree_process, pprint_pformat, regex_compile, meteor_contest, coverage, chaos

# HPT report

- Reliability score: 99.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x