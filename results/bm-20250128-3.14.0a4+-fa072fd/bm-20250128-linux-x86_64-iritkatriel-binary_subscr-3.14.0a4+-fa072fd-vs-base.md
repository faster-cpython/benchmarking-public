# Results vs. base

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: fa072fd
- commit date: 2025-01-28
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 257 ms: 1.01x slower                                                 |
| html5lib       | 61.0 ms                                                                | 62.2 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                | 23.6 ms                                                                | 22.9 ms: 1.03x faster                                                |
| async_tree_memoization    | 324 ms                                                                 | 327 ms: 1.01x slower                                                 |
| async_tree_none_tg        | 253 ms                                                                 | 256 ms: 1.01x slower                                                 |
| async_tree_memoization_tg | 313 ms                                                                 | 318 ms: 1.01x slower                                                 |
| async_tree_io_tg          | 608 ms                                                                 | 621 ms: 1.02x slower                                                 |
| async_generators          | 378 ms                                                                 | 387 ms: 1.03x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| float          | 70.9 ms                                                                | 72.1 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.32 ms                                                                | 3.18 ms: 1.04x faster                                                |
| regex_compile  | 127 ms                                                                 | 129 ms: 1.02x slower                                                 |
| regex_dna      | 210 ms                                                                 | 214 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 60.0 ms                                                                | 59.5 ms: 1.01x faster                                                |
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                |
| xml_etree_generate   | 85.4 ms                                                                | 84.8 ms: 1.01x faster                                                |
| pickle_pure_python   | 326 us                                                                 | 325 us: 1.00x faster                                                 |
| json_loads           | 28.6 us                                                                | 29.0 us: 1.01x slower                                                |
| unpickle_pure_python | 218 us                                                                 | 221 us: 1.01x slower                                                 |
| tomli_loads          | 1.93 sec                                                               | 2.05 sec: 1.06x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                |
| python_startup_no_site | 7.02 ms                                                                | 7.06 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                |
| mako            | 10.8 ms                                                                | 11.3 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20250128-linux-x86_64-python-7dd0a7e52ee832559b89-3.14.0a4+-7dd0a7e | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot              | 3.32 ms                                                                | 3.18 ms: 1.04x faster                                                |
| spectral_norm             | 101 ms                                                                 | 97.9 ms: 1.04x faster                                                |
| coroutines                | 23.6 ms                                                                | 22.9 ms: 1.03x faster                                                |
| thrift                    | 774 us                                                                 | 757 us: 1.02x faster                                                 |
| gc_traversal              | 4.91 ms                                                                | 4.81 ms: 1.02x faster                                                |
| pycparser                 | 1.16 sec                                                               | 1.14 sec: 1.02x faster                                               |
| telco                     | 7.99 ms                                                                | 7.85 ms: 1.02x faster                                                |
| coverage                  | 91.4 ms                                                                | 89.8 ms: 1.02x faster                                                |
| deepcopy_reduce           | 2.70 us                                                                | 2.66 us: 1.01x faster                                                |
| logging_format            | 6.22 us                                                                | 6.13 us: 1.01x faster                                                |
| django_template           | 32.6 ms                                                                | 32.2 ms: 1.01x faster                                                |
| scimark_fft               | 350 ms                                                                 | 346 ms: 1.01x faster                                                 |
| xml_etree_process         | 60.0 ms                                                                | 59.5 ms: 1.01x faster                                                |
| json_dumps                | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                |
| xml_etree_generate        | 85.4 ms                                                                | 84.8 ms: 1.01x faster                                                |
| deepcopy                  | 260 us                                                                 | 259 us: 1.01x faster                                                 |
| create_gc_cycles          | 2.47 ms                                                                | 2.45 ms: 1.00x faster                                                |
| pickle_pure_python        | 326 us                                                                 | 325 us: 1.00x faster                                                 |
| sqlglot_optimize          | 52.8 ms                                                                | 52.6 ms: 1.00x faster                                                |
| python_startup            | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                |
| pidigits                  | 186 ms                                                                 | 187 ms: 1.00x slower                                                 |
| sympy_sum                 | 147 ms                                                                 | 148 ms: 1.00x slower                                                 |
| python_startup_no_site    | 7.02 ms                                                                | 7.06 ms: 1.00x slower                                                |
| sqlalchemy_declarative    | 129 ms                                                                 | 130 ms: 1.01x slower                                                 |
| dulwich_log               | 64.3 ms                                                                | 64.8 ms: 1.01x slower                                                |
| meteor_contest            | 107 ms                                                                 | 107 ms: 1.01x slower                                                 |
| sympy_str                 | 266 ms                                                                 | 268 ms: 1.01x slower                                                 |
| async_tree_memoization    | 324 ms                                                                 | 327 ms: 1.01x slower                                                 |
| bench_thread_pool         | 861 us                                                                 | 867 us: 1.01x slower                                                 |
| pprint_pformat            | 1.49 sec                                                               | 1.51 sec: 1.01x slower                                               |
| sympy_integrate           | 19.7 ms                                                                | 19.9 ms: 1.01x slower                                                |
| bpe_tokeniser             | 4.49 sec                                                               | 4.53 sec: 1.01x slower                                               |
| sqlglot_transpile         | 1.56 ms                                                                | 1.58 ms: 1.01x slower                                                |
| scimark_sor               | 122 ms                                                                 | 124 ms: 1.01x slower                                                 |
| go                        | 117 ms                                                                 | 119 ms: 1.01x slower                                                 |
| sqlglot_parse             | 1.26 ms                                                                | 1.27 ms: 1.01x slower                                                |
| json_loads                | 28.6 us                                                                | 29.0 us: 1.01x slower                                                |
| async_tree_none_tg        | 253 ms                                                                 | 256 ms: 1.01x slower                                                 |
| richards                  | 44.1 ms                                                                | 44.6 ms: 1.01x slower                                                |
| 2to3                      | 254 ms                                                                 | 257 ms: 1.01x slower                                                 |
| raytrace                  | 273 ms                                                                 | 277 ms: 1.01x slower                                                 |
| unpickle_pure_python      | 218 us                                                                 | 221 us: 1.01x slower                                                 |
| async_tree_memoization_tg | 313 ms                                                                 | 318 ms: 1.01x slower                                                 |
| comprehensions            | 16.7 us                                                                | 17.0 us: 1.01x slower                                                |
| float                     | 70.9 ms                                                                | 72.1 ms: 1.02x slower                                                |
| generators                | 27.6 ms                                                                | 28.1 ms: 1.02x slower                                                |
| regex_compile             | 127 ms                                                                 | 129 ms: 1.02x slower                                                 |
| richards_super            | 50.2 ms                                                                | 51.1 ms: 1.02x slower                                                |
| regex_dna                 | 210 ms                                                                 | 214 ms: 1.02x slower                                                 |
| subparsers                | 20.5 ms                                                                | 20.9 ms: 1.02x slower                                                |
| deltablue                 | 3.21 ms                                                                | 3.27 ms: 1.02x slower                                                |
| html5lib                  | 61.0 ms                                                                | 62.2 ms: 1.02x slower                                                |
| pyflate                   | 472 ms                                                                 | 482 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 608 ms                                                                 | 621 ms: 1.02x slower                                                 |
| logging_silent            | 108 ns                                                                 | 110 ns: 1.02x slower                                                 |
| scimark_sparse_mat_mult   | 4.67 ms                                                                | 4.77 ms: 1.02x slower                                                |
| scimark_lu                | 116 ms                                                                 | 119 ms: 1.02x slower                                                 |
| async_generators          | 378 ms                                                                 | 387 ms: 1.03x slower                                                 |
| hexiom                    | 6.23 ms                                                                | 6.40 ms: 1.03x slower                                                |
| chaos                     | 58.3 ms                                                                | 60.1 ms: 1.03x slower                                                |
| nqueens                   | 81.1 ms                                                                | 83.8 ms: 1.03x slower                                                |
| fannkuch                  | 408 ms                                                                 | 423 ms: 1.03x slower                                                 |
| pathlib                   | 15.7 ms                                                                | 16.4 ms: 1.04x slower                                                |
| crypto_pyaes              | 71.7 ms                                                                | 74.9 ms: 1.04x slower                                                |
| mako                      | 10.8 ms                                                                | 11.3 ms: 1.04x slower                                                |
| tomli_loads               | 1.93 sec                                                               | 2.05 sec: 1.06x slower                                               |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (30): shortest_path, json, async_tree_cpu_io_mixed, typing_runtime_protocols, xml_etree_iterparse, sphinx, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, sympy_expand, many_optionals, asyncio_websockets, docutils, mdp, genshi_xml, genshi_text, xml_etree_parse, sqlalchemy_imperative, sqlglot_normalize, regex_v8, pprint_safe_repr, async_tree_none, async_tree_io, bench_mp_pool, deepcopy_memo, logging_simple, pylint, sqlite_synth, k_core, connected_components, nbody

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x