# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.010x faster
- HPT reliability: 92.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                         |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                       |
| html5lib       | 72.9 ms                                                      | 71.8 ms: 1.01x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 387 ms: 1.18x faster                                                         |
| async_tree_none           | 370 ms                                                       | 332 ms: 1.11x faster                                                         |
| async_tree_memoization    | 447 ms                                                       | 406 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 572 ms: 1.04x faster                                                         |
| coroutines                | 21.6 ms                                                      | 20.8 ms: 1.03x faster                                                        |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                                         |
| async_tree_io_tg          | 823 ms                                                       | 839 ms: 1.02x slower                                                         |
| async_generators          | 364 ms                                                       | 452 ms: 1.24x slower                                                         |
| Geometric mean            | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.5 ms: 1.04x faster                                                        |
| float          | 81.6 ms                                                      | 82.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.18 ms: 1.11x faster                                                        |
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| regex_v8       | 24.9 ms                                                      | 24.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| json_loads          | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| tomli_loads         | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                                       |
| pickle_pure_python  | 322 us                                                       | 336 us: 1.04x slower                                                         |
| xml_etree_iterparse | 99.8 ms                                                      | 104 ms: 1.04x slower                                                         |
| json_dumps          | 10.8 ms                                                      | 11.5 ms: 1.06x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| genshi_xml      | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                                        |
| django_template | 38.9 ms                                                      | 37.8 ms: 1.03x faster                                                        |
| mako            | 10.3 ms                                                      | 10.8 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo             | 38.9 us                                                      | 29.1 us: 1.33x faster                                                        |
| deepcopy                  | 388 us                                                       | 294 us: 1.32x faster                                                         |
| go                        | 167 ms                                                       | 136 ms: 1.23x faster                                                         |
| deepcopy_reduce           | 3.49 us                                                      | 2.92 us: 1.20x faster                                                        |
| async_tree_memoization_tg | 458 ms                                                       | 387 ms: 1.18x faster                                                         |
| generators                | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                                        |
| pylint                    | 345 ms                                                       | 307 ms: 1.12x faster                                                         |
| async_tree_none           | 370 ms                                                       | 332 ms: 1.11x faster                                                         |
| regex_effbot              | 3.51 ms                                                      | 3.18 ms: 1.11x faster                                                        |
| async_tree_memoization    | 447 ms                                                       | 406 ms: 1.10x faster                                                         |
| pathlib                   | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                        |
| genshi_text               | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| telco                     | 8.77 ms                                                      | 8.12 ms: 1.08x faster                                                        |
| json                      | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                                        |
| coverage                  | 84.5 ms                                                      | 78.5 ms: 1.08x faster                                                        |
| thrift                    | 918 us                                                       | 859 us: 1.07x faster                                                         |
| fannkuch                  | 384 ms                                                       | 362 ms: 1.06x faster                                                         |
| pprint_pformat            | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                       |
| pprint_safe_repr          | 835 ms                                                       | 796 ms: 1.05x faster                                                         |
| sqlalchemy_declarative    | 148 ms                                                       | 141 ms: 1.05x faster                                                         |
| scimark_sor               | 125 ms                                                       | 119 ms: 1.05x faster                                                         |
| bpe_tokeniser             | 5.09 sec                                                     | 4.86 sec: 1.05x faster                                                       |
| shortest_path             | 477 ms                                                       | 458 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 572 ms: 1.04x faster                                                         |
| genshi_xml                | 58.0 ms                                                      | 55.8 ms: 1.04x faster                                                        |
| nbody                     | 92.1 ms                                                      | 88.5 ms: 1.04x faster                                                        |
| richards_super            | 60.2 ms                                                      | 58.2 ms: 1.03x faster                                                        |
| coroutines                | 21.6 ms                                                      | 20.8 ms: 1.03x faster                                                        |
| meteor_contest            | 130 ms                                                       | 126 ms: 1.03x faster                                                         |
| hexiom                    | 6.47 ms                                                      | 6.28 ms: 1.03x faster                                                        |
| django_template           | 38.9 ms                                                      | 37.8 ms: 1.03x faster                                                        |
| pycparser                 | 1.28 sec                                                     | 1.25 sec: 1.03x faster                                                       |
| regex_compile             | 143 ms                                                       | 139 ms: 1.03x faster                                                         |
| 2to3                      | 293 ms                                                       | 286 ms: 1.02x faster                                                         |
| regex_v8                  | 24.9 ms                                                      | 24.5 ms: 1.02x faster                                                        |
| crypto_pyaes              | 73.5 ms                                                      | 72.4 ms: 1.02x faster                                                        |
| html5lib                  | 72.9 ms                                                      | 71.8 ms: 1.01x faster                                                        |
| connected_components      | 443 ms                                                       | 436 ms: 1.01x faster                                                         |
| richards                  | 52.5 ms                                                      | 51.8 ms: 1.01x faster                                                        |
| typing_runtime_protocols  | 176 us                                                       | 173 us: 1.01x faster                                                         |
| asyncio_websockets        | 395 ms                                                       | 390 ms: 1.01x faster                                                         |
| sympy_expand              | 506 ms                                                       | 502 ms: 1.01x faster                                                         |
| sympy_str                 | 297 ms                                                       | 295 ms: 1.01x faster                                                         |
| nqueens                   | 92.3 ms                                                      | 91.7 ms: 1.01x faster                                                        |
| scimark_lu                | 97.4 ms                                                      | 96.9 ms: 1.01x faster                                                        |
| python_startup_no_site    | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                        |
| mdp                       | 2.53 sec                                                     | 2.54 sec: 1.00x slower                                                       |
| sympy_integrate           | 23.4 ms                                                      | 23.7 ms: 1.01x slower                                                        |
| pyflate                   | 493 ms                                                       | 499 ms: 1.01x slower                                                         |
| sqlglot_normalize         | 119 ms                                                       | 120 ms: 1.01x slower                                                         |
| scimark_monte_carlo       | 65.2 ms                                                      | 66.2 ms: 1.01x slower                                                        |
| float                     | 81.6 ms                                                      | 82.9 ms: 1.02x slower                                                        |
| xml_etree_parse           | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| sphinx                    | 1.11 sec                                                     | 1.13 sec: 1.02x slower                                                       |
| async_tree_io_tg          | 823 ms                                                       | 839 ms: 1.02x slower                                                         |
| sqlglot_optimize          | 58.7 ms                                                      | 59.9 ms: 1.02x slower                                                        |
| comprehensions            | 17.3 us                                                      | 17.7 us: 1.02x slower                                                        |
| sqlglot_transpile         | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                        |
| python_startup            | 15.6 ms                                                      | 16.0 ms: 1.02x slower                                                        |
| chaos                     | 60.6 ms                                                      | 62.2 ms: 1.03x slower                                                        |
| spectral_norm             | 97.4 ms                                                      | 100 ms: 1.03x slower                                                         |
| json_loads                | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| tomli_loads               | 2.43 sec                                                     | 2.52 sec: 1.04x slower                                                       |
| docutils                  | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                       |
| sqlglot_parse             | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                        |
| logging_format            | 6.95 us                                                      | 7.24 us: 1.04x slower                                                        |
| pickle_pure_python        | 322 us                                                       | 336 us: 1.04x slower                                                         |
| xml_etree_iterparse       | 99.8 ms                                                      | 104 ms: 1.04x slower                                                         |
| deltablue                 | 3.38 ms                                                      | 3.54 ms: 1.04x slower                                                        |
| dulwich_log               | 65.5 ms                                                      | 68.5 ms: 1.05x slower                                                        |
| mako                      | 10.3 ms                                                      | 10.8 ms: 1.05x slower                                                        |
| logging_silent            | 97.5 ns                                                      | 103 ns: 1.05x slower                                                         |
| raytrace                  | 267 ms                                                       | 282 ms: 1.05x slower                                                         |
| scimark_fft               | 298 ms                                                       | 315 ms: 1.06x slower                                                         |
| logging_simple            | 6.28 us                                                      | 6.63 us: 1.06x slower                                                        |
| json_dumps                | 10.8 ms                                                      | 11.5 ms: 1.06x slower                                                        |
| create_gc_cycles          | 2.65 ms                                                      | 2.95 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.79 ms: 1.14x slower                                                        |
| k_core                    | 2.18 sec                                                     | 2.63 sec: 1.21x slower                                                       |
| async_generators          | 364 ms                                                       | 452 ms: 1.24x slower                                                         |
| gc_traversal              | 4.48 ms                                                      | 6.20 ms: 1.38x slower                                                        |
| bench_mp_pool             | 4.82 ms                                                      | 1.40 sec: 289.86x slower                                                     |
| Geometric mean            | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, async_tree_none_tg, xml_etree_generate, pidigits, xml_etree_process, sympy_sum, bench_thread_pool, regex_dna, unpickle_pure_python, sqlalchemy_imperative, async_tree_io
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 92.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x