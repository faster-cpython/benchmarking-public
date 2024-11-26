# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.102x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 389 ms: 1.28x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.70 sec: 1.28x slower                                                   |
| html5lib       | 66.4 ms                                                  | 72.7 ms: 1.10x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                   |
| tornado_http   | 128 ms                                                   | 148 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                    | 1.21x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 565 ms: 1.15x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 597 ms: 1.09x faster                                                     |
| async_tree_none           | 497 ms                                                   | 468 ms: 1.06x faster                                                     |
| coroutines                | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                    |
| async_generators          | 489 ms                                                   | 519 ms: 1.06x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.06x slower                                                   |
| async_tree_io_tg          | 1.13 sec                                                 | 1.24 sec: 1.09x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                    |
| regex_dna      | 253 ms                                                   | 250 ms: 1.01x faster                                                     |
| regex_effbot   | 4.89 ms                                                  | 5.27 ms: 1.08x slower                                                    |
| regex_compile  | 127 ms                                                   | 175 ms: 1.38x slower                                                     |
| Geometric mean | (ref)                                                    | 1.09x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.05x faster                                                     |
| xml_etree_generate   | 113 ms                                                   | 112 ms: 1.02x faster                                                     |
| json_loads           | 31.7 us                                                  | 31.5 us: 1.01x faster                                                    |
| json_dumps           | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.68 sec: 1.05x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 391 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 15.6 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                    |
| genshi_text     | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                    |
| django_template | 41.6 ms                                                  | 53.0 ms: 1.27x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 82.8 ms: 1.37x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 39.3 us: 1.28x faster                                                    |
| deepcopy                  | 447 us                                                   | 383 us: 1.17x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 565 ms: 1.15x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 597 ms: 1.09x faster                                                     |
| async_tree_none           | 497 ms                                                   | 468 ms: 1.06x faster                                                     |
| xml_etree_parse           | 197 ms                                                   | 186 ms: 1.05x faster                                                     |
| pathlib                   | 22.7 ms                                                  | 21.5 ms: 1.05x faster                                                    |
| scimark_sor               | 160 ms                                                   | 155 ms: 1.03x faster                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 3.95 us: 1.03x faster                                                    |
| regex_v8                  | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                    |
| telco                     | 9.74 ms                                                  | 9.50 ms: 1.03x faster                                                    |
| xml_etree_generate        | 113 ms                                                   | 112 ms: 1.02x faster                                                     |
| regex_dna                 | 253 ms                                                   | 250 ms: 1.01x faster                                                     |
| mako                      | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                    |
| json_loads                | 31.7 us                                                  | 31.5 us: 1.01x faster                                                    |
| logging_silent            | 133 ns                                                   | 135 ns: 1.01x slower                                                     |
| python_startup            | 15.4 ms                                                  | 15.6 ms: 1.01x slower                                                    |
| coroutines                | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                    |
| bpe_tokeniser             | 5.87 sec                                                 | 5.97 sec: 1.02x slower                                                   |
| scimark_fft               | 447 ms                                                   | 461 ms: 1.03x slower                                                     |
| float                     | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                    |
| json_dumps                | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.51 sec: 1.05x slower                                                   |
| tomli_loads               | 2.54 sec                                                 | 2.68 sec: 1.05x slower                                                   |
| logging_format            | 7.82 us                                                  | 8.25 us: 1.05x slower                                                    |
| scimark_monte_carlo       | 83.6 ms                                                  | 88.7 ms: 1.06x slower                                                    |
| async_generators          | 489 ms                                                   | 519 ms: 1.06x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.06x slower                                                   |
| unpickle_pure_python      | 251 us                                                   | 268 us: 1.07x slower                                                     |
| crypto_pyaes              | 83.7 ms                                                  | 89.9 ms: 1.07x slower                                                    |
| logging_simple            | 7.07 us                                                  | 7.62 us: 1.08x slower                                                    |
| bench_thread_pool         | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                                    |
| regex_effbot              | 4.89 ms                                                  | 5.27 ms: 1.08x slower                                                    |
| meteor_contest            | 114 ms                                                   | 124 ms: 1.09x slower                                                     |
| spectral_norm             | 143 ms                                                   | 155 ms: 1.09x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.65 ms: 1.09x slower                                                    |
| async_tree_io_tg          | 1.13 sec                                                 | 1.24 sec: 1.09x slower                                                   |
| scimark_lu                | 139 ms                                                   | 152 ms: 1.09x slower                                                     |
| fannkuch                  | 461 ms                                                   | 505 ms: 1.10x slower                                                     |
| html5lib                  | 66.4 ms                                                  | 72.7 ms: 1.10x slower                                                    |
| pickle_pure_python        | 357 us                                                   | 391 us: 1.10x slower                                                     |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.14 ms: 1.10x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.35 ms: 1.10x slower                                                    |
| typing_runtime_protocols  | 193 us                                                   | 219 us: 1.13x slower                                                     |
| pyflate                   | 556 ms                                                   | 643 ms: 1.16x slower                                                     |
| go                        | 160 ms                                                   | 185 ms: 1.16x slower                                                     |
| raytrace                  | 300 ms                                                   | 347 ms: 1.16x slower                                                     |
| tornado_http              | 128 ms                                                   | 148 ms: 1.16x slower                                                     |
| richards_super            | 60.1 ms                                                  | 70.5 ms: 1.17x slower                                                    |
| pycparser                 | 1.27 sec                                                 | 1.51 sec: 1.19x slower                                                   |
| deltablue                 | 3.82 ms                                                  | 4.54 ms: 1.19x slower                                                    |
| richards                  | 53.6 ms                                                  | 64.9 ms: 1.21x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                    |
| sqlalchemy_imperative     | 15.1 ms                                                  | 18.8 ms: 1.24x slower                                                    |
| sqlglot_normalize         | 127 ms                                                   | 157 ms: 1.24x slower                                                     |
| comprehensions            | 20.4 us                                                  | 25.3 us: 1.24x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.72 ms: 1.25x slower                                                    |
| sphinx                    | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                   |
| nqueens                   | 100 ms                                                   | 126 ms: 1.26x slower                                                     |
| sqlalchemy_declarative    | 150 ms                                                   | 190 ms: 1.26x slower                                                     |
| sqlglot_transpile         | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                    |
| chaos                     | 68.0 ms                                                  | 86.1 ms: 1.27x slower                                                    |
| django_template           | 41.6 ms                                                  | 53.0 ms: 1.27x slower                                                    |
| 2to3                      | 304 ms                                                   | 389 ms: 1.28x slower                                                     |
| docutils                  | 2.89 sec                                                 | 3.70 sec: 1.28x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.19 sec: 1.29x slower                                                   |
| sympy_expand              | 457 ms                                                   | 600 ms: 1.31x slower                                                     |
| pprint_pformat            | 1.90 sec                                                 | 2.51 sec: 1.32x slower                                                   |
| sqlglot_optimize          | 62.2 ms                                                  | 83.4 ms: 1.34x slower                                                    |
| sympy_str                 | 264 ms                                                   | 362 ms: 1.37x slower                                                     |
| genshi_xml                | 60.3 ms                                                  | 82.8 ms: 1.37x slower                                                    |
| regex_compile             | 127 ms                                                   | 175 ms: 1.38x slower                                                     |
| pylint                    | 342 ms                                                   | 489 ms: 1.43x slower                                                     |
| sympy_integrate           | 20.8 ms                                                  | 29.9 ms: 1.44x slower                                                    |
| hexiom                    | 7.11 ms                                                  | 10.5 ms: 1.47x slower                                                    |
| sympy_sum                 | 144 ms                                                   | 222 ms: 1.55x slower                                                     |
| generators                | 37.6 ms                                                  | 58.8 ms: 1.56x slower                                                    |
| bench_mp_pool             | 7.68 ms                                                  | 1.47 sec: 191.36x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, coverage, nbody, json, async_tree_cpu_io_mixed, async_tree_none_tg, xml_etree_iterparse, pidigits, asyncio_websockets, python_startup_no_site, thrift, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: dulwich_log

- Geometric mean (including insignificant results): 1.102x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.08x