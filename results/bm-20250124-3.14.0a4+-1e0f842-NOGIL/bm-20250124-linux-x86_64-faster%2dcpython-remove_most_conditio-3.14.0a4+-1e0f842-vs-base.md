# Results vs. base

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.007x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                 | 311 ms: 1.01x slower                                                             |
| html5lib       | 69.4 ms                                                                | 68.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators | 440 ms                                                                 | 442 ms: 1.00x slower                                                             |
| coroutines       | 25.3 ms                                                                | 25.9 ms: 1.02x slower                                                            |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets, async_tree_none, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.0 ms                                                                | 79.9 ms: 1.02x slower                                                            |
| pidigits       | 181 ms                                                                 | 190 ms: 1.05x slower                                                             |
| nbody          | 135 ms                                                                 | 147 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.35 ms                                                                | 3.28 ms: 1.02x faster                                                            |
| regex_dna      | 222 ms                                                                 | 218 ms: 1.02x faster                                                             |
| regex_compile  | 149 ms                                                                 | 151 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 94.9 ms                                                                | 95.3 ms: 1.00x slower                                                            |
| pickle_pure_python   | 372 us                                                                 | 374 us: 1.01x slower                                                             |
| xml_etree_process    | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| xml_etree_generate   | 95.3 ms                                                                | 96.2 ms: 1.01x slower                                                            |
| json_dumps           | 12.6 ms                                                                | 12.7 ms: 1.01x slower                                                            |
| unpickle_pure_python | 255 us                                                                 | 258 us: 1.01x slower                                                             |
| tomli_loads          | 2.36 sec                                                               | 2.44 sec: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                                | 9.38 ms: 1.00x slower                                                            |
| python_startup         | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 41.4 ms                                                                | 41.7 ms: 1.01x slower                                                            |
| genshi_text     | 28.1 ms                                                                | 28.7 ms: 1.02x slower                                                            |
| mako            | 16.4 ms                                                                | 16.8 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250123-linux-x86_64-python-a10f99375e7912df863c-3.14.0a4+-a10f993 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                      | 2.86 sec                                                               | 2.76 sec: 1.04x faster                                                           |
| logging_silent           | 122 ns                                                                 | 119 ns: 1.02x faster                                                             |
| regex_effbot             | 3.35 ms                                                                | 3.28 ms: 1.02x faster                                                            |
| sqlite_synth             | 2.76 us                                                                | 2.71 us: 1.02x faster                                                            |
| regex_dna                | 222 ms                                                                 | 218 ms: 1.02x faster                                                             |
| create_gc_cycles         | 1.73 ms                                                                | 1.70 ms: 1.02x faster                                                            |
| json                     | 5.62 ms                                                                | 5.56 ms: 1.01x faster                                                            |
| pathlib                  | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                                            |
| connected_components     | 531 ms                                                                 | 526 ms: 1.01x faster                                                             |
| html5lib                 | 69.4 ms                                                                | 68.8 ms: 1.01x faster                                                            |
| nqueens                  | 100 ms                                                                 | 99.6 ms: 1.01x faster                                                            |
| scimark_lu               | 142 ms                                                                 | 141 ms: 1.01x faster                                                             |
| shortest_path            | 572 ms                                                                 | 569 ms: 1.00x faster                                                             |
| deepcopy                 | 314 us                                                                 | 313 us: 1.00x faster                                                             |
| k_core                   | 2.46 sec                                                               | 2.46 sec: 1.00x faster                                                           |
| crypto_pyaes             | 90.9 ms                                                                | 91.1 ms: 1.00x slower                                                            |
| python_startup_no_site   | 9.36 ms                                                                | 9.38 ms: 1.00x slower                                                            |
| deepcopy_reduce          | 3.30 us                                                                | 3.31 us: 1.00x slower                                                            |
| python_startup           | 15.0 ms                                                                | 15.1 ms: 1.00x slower                                                            |
| hexiom                   | 7.84 ms                                                                | 7.87 ms: 1.00x slower                                                            |
| async_generators         | 440 ms                                                                 | 442 ms: 1.00x slower                                                             |
| xml_etree_iterparse      | 94.9 ms                                                                | 95.3 ms: 1.00x slower                                                            |
| bpe_tokeniser            | 5.07 sec                                                               | 5.10 sec: 1.00x slower                                                           |
| raytrace                 | 355 ms                                                                 | 357 ms: 1.01x slower                                                             |
| thrift                   | 946 us                                                                 | 951 us: 1.01x slower                                                             |
| pickle_pure_python       | 372 us                                                                 | 374 us: 1.01x slower                                                             |
| deepcopy_memo            | 39.6 us                                                                | 39.8 us: 1.01x slower                                                            |
| xml_etree_process        | 68.3 ms                                                                | 68.7 ms: 1.01x slower                                                            |
| many_optionals           | 1.09 ms                                                                | 1.10 ms: 1.01x slower                                                            |
| pycparser                | 1.18 sec                                                               | 1.19 sec: 1.01x slower                                                           |
| go                       | 143 ms                                                                 | 144 ms: 1.01x slower                                                             |
| django_template          | 41.4 ms                                                                | 41.7 ms: 1.01x slower                                                            |
| sympy_expand             | 529 ms                                                                 | 533 ms: 1.01x slower                                                             |
| 2to3                     | 308 ms                                                                 | 311 ms: 1.01x slower                                                             |
| chaos                    | 74.0 ms                                                                | 74.6 ms: 1.01x slower                                                            |
| pprint_safe_repr         | 853 ms                                                                 | 861 ms: 1.01x slower                                                             |
| sqlglot_optimize         | 60.5 ms                                                                | 61.1 ms: 1.01x slower                                                            |
| scimark_sor              | 142 ms                                                                 | 143 ms: 1.01x slower                                                             |
| xml_etree_generate       | 95.3 ms                                                                | 96.2 ms: 1.01x slower                                                            |
| typing_runtime_protocols | 209 us                                                                 | 211 us: 1.01x slower                                                             |
| subparsers               | 24.3 ms                                                                | 24.6 ms: 1.01x slower                                                            |
| regex_compile            | 149 ms                                                                 | 151 ms: 1.01x slower                                                             |
| json_dumps               | 12.6 ms                                                                | 12.7 ms: 1.01x slower                                                            |
| coverage                 | 106 ms                                                                 | 107 ms: 1.01x slower                                                             |
| pprint_pformat           | 1.76 sec                                                               | 1.77 sec: 1.01x slower                                                           |
| sympy_integrate          | 23.8 ms                                                                | 24.1 ms: 1.01x slower                                                            |
| dulwich_log              | 68.9 ms                                                                | 69.7 ms: 1.01x slower                                                            |
| telco                    | 9.17 ms                                                                | 9.28 ms: 1.01x slower                                                            |
| unpickle_pure_python     | 255 us                                                                 | 258 us: 1.01x slower                                                             |
| sympy_str                | 318 ms                                                                 | 322 ms: 1.01x slower                                                             |
| logging_simple           | 6.65 us                                                                | 6.74 us: 1.01x slower                                                            |
| sqlglot_transpile        | 1.95 ms                                                                | 1.98 ms: 1.01x slower                                                            |
| sympy_sum                | 176 ms                                                                 | 179 ms: 1.01x slower                                                             |
| scimark_fft              | 420 ms                                                                 | 426 ms: 1.02x slower                                                             |
| generators               | 31.3 ms                                                                | 31.8 ms: 1.02x slower                                                            |
| fannkuch                 | 516 ms                                                                 | 524 ms: 1.02x slower                                                             |
| scimark_sparse_mat_mult  | 6.16 ms                                                                | 6.27 ms: 1.02x slower                                                            |
| sqlalchemy_declarative   | 162 ms                                                                 | 165 ms: 1.02x slower                                                             |
| scimark_monte_carlo      | 86.3 ms                                                                | 87.8 ms: 1.02x slower                                                            |
| deltablue                | 4.74 ms                                                                | 4.83 ms: 1.02x slower                                                            |
| genshi_text              | 28.1 ms                                                                | 28.7 ms: 1.02x slower                                                            |
| sqlglot_parse            | 1.55 ms                                                                | 1.58 ms: 1.02x slower                                                            |
| spectral_norm            | 115 ms                                                                 | 117 ms: 1.02x slower                                                             |
| sqlglot_normalize        | 120 ms                                                                 | 122 ms: 1.02x slower                                                             |
| richards_super           | 63.2 ms                                                                | 64.5 ms: 1.02x slower                                                            |
| coroutines               | 25.3 ms                                                                | 25.9 ms: 1.02x slower                                                            |
| comprehensions           | 20.6 us                                                                | 21.1 us: 1.02x slower                                                            |
| float                    | 78.0 ms                                                                | 79.9 ms: 1.02x slower                                                            |
| mako                     | 16.4 ms                                                                | 16.8 ms: 1.03x slower                                                            |
| tomli_loads              | 2.36 sec                                                               | 2.44 sec: 1.04x slower                                                           |
| pyflate                  | 526 ms                                                                 | 545 ms: 1.04x slower                                                             |
| gc_traversal             | 4.44 ms                                                                | 4.61 ms: 1.04x slower                                                            |
| pidigits                 | 181 ms                                                                 | 190 ms: 1.05x slower                                                             |
| nbody                    | 135 ms                                                                 | 147 ms: 1.08x slower                                                             |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (22): sqlalchemy_imperative, sphinx, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, richards, meteor_contest, bench_thread_pool, async_tree_cpu_io_mixed, async_tree_io_tg, docutils, asyncio_websockets, async_tree_none, async_tree_memoization_tg, logging_format, json_loads, bench_mp_pool, xml_etree_parse, regex_v8, async_tree_memoization, genshi_xml, pylint

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x