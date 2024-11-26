# Results vs. 3.13.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: linux-aarch64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 402 ms: 1.33x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.78 sec: 1.31x slower                                                   |
| html5lib       | 66.4 ms                                                  | 72.9 ms: 1.10x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| Geometric mean | (ref)                                                    | 1.26x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 560 ms: 1.16x faster                                                     |
| async_tree_none           | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 624 ms: 1.04x faster                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                   |
| async_generators          | 489 ms                                                   | 533 ms: 1.09x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                                    |
| regex_dna      | 253 ms                                                   | 263 ms: 1.04x slower                                                     |
| regex_compile  | 127 ms                                                   | 179 ms: 1.41x slower                                                     |
| Geometric mean | (ref)                                                    | 1.11x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 274 us: 1.10x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 15.0 ms: 1.11x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 412 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, xml_etree_generate, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.04 ms: 1.04x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 50.5 ms: 1.21x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 34.7 ms: 1.25x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 84.9 ms: 1.41x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 41.7 us: 1.21x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 560 ms: 1.16x faster                                                     |
| deepcopy                  | 447 us                                                   | 407 us: 1.10x faster                                                     |
| async_tree_none           | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 624 ms: 1.04x faster                                                     |
| regex_effbot              | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                                    |
| shortest_path             | 565 ms                                                   | 580 ms: 1.03x slower                                                     |
| tomli_loads               | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                   |
| python_startup_no_site    | 8.73 ms                                                  | 9.04 ms: 1.04x slower                                                    |
| thrift                    | 968 us                                                   | 1.00 ms: 1.04x slower                                                    |
| regex_dna                 | 253 ms                                                   | 263 ms: 1.04x slower                                                     |
| connected_components      | 533 ms                                                   | 555 ms: 1.04x slower                                                     |
| logging_silent            | 133 ns                                                   | 140 ns: 1.05x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| logging_format            | 7.82 us                                                  | 8.30 us: 1.06x slower                                                    |
| logging_simple            | 7.07 us                                                  | 7.58 us: 1.07x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                   |
| bench_thread_pool         | 1.27 ms                                                  | 1.38 ms: 1.08x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.62 sec: 1.08x slower                                                   |
| fannkuch                  | 461 ms                                                   | 500 ms: 1.08x slower                                                     |
| async_generators          | 489 ms                                                   | 533 ms: 1.09x slower                                                     |
| gc_traversal              | 5.77 ms                                                  | 6.30 ms: 1.09x slower                                                    |
| unpickle_pure_python      | 251 us                                                   | 274 us: 1.10x slower                                                     |
| spectral_norm             | 143 ms                                                   | 156 ms: 1.10x slower                                                     |
| scimark_lu                | 139 ms                                                   | 153 ms: 1.10x slower                                                     |
| html5lib                  | 66.4 ms                                                  | 72.9 ms: 1.10x slower                                                    |
| pyflate                   | 556 ms                                                   | 612 ms: 1.10x slower                                                     |
| scimark_monte_carlo       | 83.6 ms                                                  | 91.9 ms: 1.10x slower                                                    |
| json_dumps                | 13.6 ms                                                  | 15.0 ms: 1.11x slower                                                    |
| crypto_pyaes              | 83.7 ms                                                  | 93.1 ms: 1.11x slower                                                    |
| meteor_contest            | 114 ms                                                   | 127 ms: 1.12x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                   |
| deltablue                 | 3.82 ms                                                  | 4.30 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.33 ms: 1.13x slower                                                    |
| typing_runtime_protocols  | 193 us                                                   | 219 us: 1.13x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.84 ms: 1.15x slower                                                    |
| pickle_pure_python        | 357 us                                                   | 412 us: 1.16x slower                                                     |
| richards                  | 53.6 ms                                                  | 63.5 ms: 1.18x slower                                                    |
| go                        | 160 ms                                                   | 189 ms: 1.19x slower                                                     |
| pycparser                 | 1.27 sec                                                 | 1.51 sec: 1.19x slower                                                   |
| comprehensions            | 20.4 us                                                  | 24.4 us: 1.20x slower                                                    |
| raytrace                  | 300 ms                                                   | 362 ms: 1.21x slower                                                     |
| django_template           | 41.6 ms                                                  | 50.5 ms: 1.21x slower                                                    |
| richards_super            | 60.1 ms                                                  | 73.6 ms: 1.22x slower                                                    |
| chaos                     | 68.0 ms                                                  | 84.3 ms: 1.24x slower                                                    |
| nqueens                   | 100 ms                                                   | 124 ms: 1.24x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 34.7 ms: 1.25x slower                                                    |
| pylint                    | 342 ms                                                   | 433 ms: 1.27x slower                                                     |
| sqlglot_transpile         | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                                    |
| sqlglot_normalize         | 127 ms                                                   | 162 ms: 1.28x slower                                                     |
| sqlalchemy_imperative     | 15.1 ms                                                  | 19.6 ms: 1.30x slower                                                    |
| sympy_expand              | 457 ms                                                   | 597 ms: 1.31x slower                                                     |
| docutils                  | 2.89 sec                                                 | 3.78 sec: 1.31x slower                                                   |
| sqlalchemy_declarative    | 150 ms                                                   | 197 ms: 1.31x slower                                                     |
| sphinx                    | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| 2to3                      | 304 ms                                                   | 402 ms: 1.33x slower                                                     |
| generators                | 37.6 ms                                                  | 50.4 ms: 1.34x slower                                                    |
| pprint_safe_repr          | 926 ms                                                   | 1.26 sec: 1.36x slower                                                   |
| sympy_str                 | 264 ms                                                   | 362 ms: 1.37x slower                                                     |
| sqlglot_optimize          | 62.2 ms                                                  | 85.5 ms: 1.37x slower                                                    |
| sympy_integrate           | 20.8 ms                                                  | 28.9 ms: 1.39x slower                                                    |
| hexiom                    | 7.11 ms                                                  | 9.88 ms: 1.39x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.66 sec: 1.40x slower                                                   |
| genshi_xml                | 60.3 ms                                                  | 84.9 ms: 1.41x slower                                                    |
| regex_compile             | 127 ms                                                   | 179 ms: 1.41x slower                                                     |
| sympy_sum                 | 144 ms                                                   | 212 ms: 1.48x slower                                                     |
| k_core                    | 2.96 sec                                                 | 4.55 sec: 1.54x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 1.58 sec: 206.15x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (23): xml_etree_parse, async_tree_none_tg, scimark_fft, scimark_sor, pathlib, async_tree_cpu_io_mixed, nbody, async_tree_cpu_io_mixed_tg, bpe_tokeniser, xml_etree_iterparse, json, deepcopy_reduce, coverage, xml_etree_generate, coroutines, mako, json_loads, telco, asyncio_websockets, regex_v8, xml_etree_process, float, pidigits
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.096x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x