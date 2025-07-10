# Results vs. base

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: linux-x86_64
- commit hash: 6365919
- commit date: 2025-07-10
- overall geometric mean: 1.008x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| html5lib       | 67.0 ms                                                                     | 65.9 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|-------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization  | 333 ms                                                                      | 325 ms: 1.02x faster                                                                 |
| async_tree_io           | 626 ms                                                                      | 614 ms: 1.02x faster                                                                 |
| async_tree_io_tg        | 635 ms                                                                      | 627 ms: 1.01x faster                                                                 |
| async_tree_none         | 272 ms                                                                      | 269 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed | 502 ms                                                                      | 496 ms: 1.01x faster                                                                 |
| asyncio_websockets      | 381 ms                                                                      | 383 ms: 1.00x slower                                                                 |
| coroutines              | 22.3 ms                                                                     | 22.9 ms: 1.03x slower                                                                |
| async_generators        | 417 ms                                                                      | 435 ms: 1.04x slower                                                                 |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 72.6 ms                                                                     | 70.4 ms: 1.03x faster                                                                |
| nbody          | 96.4 ms                                                                     | 94.7 ms: 1.02x faster                                                                |
| pidigits       | 256 ms                                                                      | 256 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                                      | 131 ms: 1.01x faster                                                                 |
| regex_effbot   | 3.46 ms                                                                     | 3.50 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 25.4 us                                                                     | 25.0 us: 1.02x faster                                                                |
| tomli_loads          | 2.04 sec                                                                    | 2.02 sec: 1.01x faster                                                               |
| pickle_pure_python   | 331 us                                                                      | 328 us: 1.01x faster                                                                 |
| xml_etree_process    | 58.5 ms                                                                     | 58.2 ms: 1.01x faster                                                                |
| xml_etree_parse      | 139 ms                                                                      | 138 ms: 1.01x faster                                                                 |
| unpickle_pure_python | 209 us                                                                      | 208 us: 1.00x faster                                                                 |
| xml_etree_generate   | 83.5 ms                                                                     | 84.4 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.86 ms                                                                     | 8.77 ms: 1.01x faster                                                                |
| python_startup         | 15.4 ms                                                                     | 15.2 ms: 1.01x faster                                                                |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250710-pythonperf2-x86_64-python-c17654334946b232aa29-3.15.0a0-c176543 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| gc_traversal             | 6.53 ms                                                                     | 5.88 ms: 1.11x faster                                                                |
| create_gc_cycles         | 2.99 ms                                                                     | 2.77 ms: 1.08x faster                                                                |
| pyflate                  | 433 ms                                                                      | 409 ms: 1.06x faster                                                                 |
| pprint_safe_repr         | 779 ms                                                                      | 748 ms: 1.04x faster                                                                 |
| deepcopy_memo            | 28.2 us                                                                     | 27.1 us: 1.04x faster                                                                |
| pprint_pformat           | 1.58 sec                                                                    | 1.53 sec: 1.04x faster                                                               |
| scimark_monte_carlo      | 62.3 ms                                                                     | 60.2 ms: 1.03x faster                                                                |
| float                    | 72.6 ms                                                                     | 70.4 ms: 1.03x faster                                                                |
| scimark_fft              | 316 ms                                                                      | 307 ms: 1.03x faster                                                                 |
| spectral_norm            | 87.2 ms                                                                     | 85.2 ms: 1.02x faster                                                                |
| deepcopy                 | 275 us                                                                      | 268 us: 1.02x faster                                                                 |
| async_tree_memoization   | 333 ms                                                                      | 325 ms: 1.02x faster                                                                 |
| scimark_sparse_mat_mult  | 4.97 ms                                                                     | 4.87 ms: 1.02x faster                                                                |
| deepcopy_reduce          | 2.99 us                                                                     | 2.93 us: 1.02x faster                                                                |
| richards                 | 46.0 ms                                                                     | 45.1 ms: 1.02x faster                                                                |
| coverage                 | 81.8 ms                                                                     | 80.3 ms: 1.02x faster                                                                |
| async_tree_io            | 626 ms                                                                      | 614 ms: 1.02x faster                                                                 |
| json                     | 5.36 ms                                                                     | 5.26 ms: 1.02x faster                                                                |
| nbody                    | 96.4 ms                                                                     | 94.7 ms: 1.02x faster                                                                |
| json_loads               | 25.4 us                                                                     | 25.0 us: 1.02x faster                                                                |
| richards_super           | 52.0 ms                                                                     | 51.1 ms: 1.02x faster                                                                |
| html5lib                 | 67.0 ms                                                                     | 65.9 ms: 1.02x faster                                                                |
| regex_compile            | 132 ms                                                                      | 131 ms: 1.01x faster                                                                 |
| typing_runtime_protocols | 169 us                                                                      | 166 us: 1.01x faster                                                                 |
| async_tree_io_tg         | 635 ms                                                                      | 627 ms: 1.01x faster                                                                 |
| crypto_pyaes             | 75.8 ms                                                                     | 74.9 ms: 1.01x faster                                                                |
| async_tree_none          | 272 ms                                                                      | 269 ms: 1.01x faster                                                                 |
| sqlglot_v2_transpile     | 1.69 ms                                                                     | 1.67 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed  | 502 ms                                                                      | 496 ms: 1.01x faster                                                                 |
| sqlite_synth             | 2.88 us                                                                     | 2.85 us: 1.01x faster                                                                |
| python_startup_no_site   | 8.86 ms                                                                     | 8.77 ms: 1.01x faster                                                                |
| tomli_loads              | 2.04 sec                                                                    | 2.02 sec: 1.01x faster                                                               |
| scimark_sor              | 104 ms                                                                      | 103 ms: 1.01x faster                                                                 |
| pickle_pure_python       | 331 us                                                                      | 328 us: 1.01x faster                                                                 |
| python_startup           | 15.4 ms                                                                     | 15.2 ms: 1.01x faster                                                                |
| bpe_tokeniser            | 4.73 sec                                                                    | 4.69 sec: 1.01x faster                                                               |
| telco                    | 159 ms                                                                      | 158 ms: 1.01x faster                                                                 |
| sqlglot_v2_parse         | 1.31 ms                                                                     | 1.30 ms: 1.01x faster                                                                |
| nqueens                  | 93.4 ms                                                                     | 92.8 ms: 1.01x faster                                                                |
| deltablue                | 3.17 ms                                                                     | 3.15 ms: 1.01x faster                                                                |
| sqlglot_v2_normalize     | 113 ms                                                                      | 112 ms: 1.01x faster                                                                 |
| xml_etree_process        | 58.5 ms                                                                     | 58.2 ms: 1.01x faster                                                                |
| pathlib                  | 17.0 ms                                                                     | 16.9 ms: 1.01x faster                                                                |
| xml_etree_parse          | 139 ms                                                                      | 138 ms: 1.01x faster                                                                 |
| many_optionals           | 1.04 ms                                                                     | 1.04 ms: 1.00x faster                                                                |
| unpickle_pure_python     | 209 us                                                                      | 208 us: 1.00x faster                                                                 |
| chaos                    | 58.5 ms                                                                     | 58.2 ms: 1.00x faster                                                                |
| pidigits                 | 256 ms                                                                      | 256 ms: 1.00x faster                                                                 |
| meteor_contest           | 120 ms                                                                      | 120 ms: 1.00x faster                                                                 |
| sympy_integrate          | 21.9 ms                                                                     | 22.0 ms: 1.00x slower                                                                |
| connected_components     | 422 ms                                                                      | 423 ms: 1.00x slower                                                                 |
| asyncio_websockets       | 381 ms                                                                      | 383 ms: 1.00x slower                                                                 |
| sympy_sum                | 150 ms                                                                      | 150 ms: 1.01x slower                                                                 |
| shortest_path            | 450 ms                                                                      | 453 ms: 1.01x slower                                                                 |
| go                       | 117 ms                                                                      | 118 ms: 1.01x slower                                                                 |
| thrift                   | 850 us                                                                      | 857 us: 1.01x slower                                                                 |
| mdp                      | 1.27 sec                                                                    | 1.28 sec: 1.01x slower                                                               |
| xml_etree_generate       | 83.5 ms                                                                     | 84.4 ms: 1.01x slower                                                                |
| sympy_str                | 283 ms                                                                      | 286 ms: 1.01x slower                                                                 |
| regex_effbot             | 3.46 ms                                                                     | 3.50 ms: 1.01x slower                                                                |
| sympy_expand             | 481 ms                                                                      | 487 ms: 1.01x slower                                                                 |
| comprehensions           | 16.2 us                                                                     | 16.5 us: 1.02x slower                                                                |
| subparsers               | 24.8 ms                                                                     | 25.3 ms: 1.02x slower                                                                |
| coroutines               | 22.3 ms                                                                     | 22.9 ms: 1.03x slower                                                                |
| async_generators         | 417 ms                                                                      | 435 ms: 1.04x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (28): pycparser, async_tree_memoization_tg, genshi_xml, fannkuch, mako, generators, async_tree_none_tg, logging_format, async_tree_cpu_io_mixed_tg, logging_silent, django_template, logging_simple, regex_dna, k_core, djangocms, json_dumps, 2to3, docutils, sphinx, sqlglot_v2_optimize, dulwich_log, genshi_text, hexiom, scimark_lu, raytrace, pylint, xml_etree_iterparse, regex_v8

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x