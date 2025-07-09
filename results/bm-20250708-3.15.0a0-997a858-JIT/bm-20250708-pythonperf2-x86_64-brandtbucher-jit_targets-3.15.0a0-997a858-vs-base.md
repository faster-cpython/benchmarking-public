# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: linux-x86_64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.001x faster
- HPT reliability: 94.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                      | 287 ms: 1.00x faster                                                     |
| docutils       | 2.93 sec                                                                    | 2.90 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 335 ms                                                                      | 330 ms: 1.02x faster                                                     |
| async_tree_io              | 632 ms                                                                      | 626 ms: 1.01x faster                                                     |
| async_tree_memoization_tg  | 335 ms                                                                      | 333 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 514 ms                                                                      | 510 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed    | 507 ms                                                                      | 503 ms: 1.01x faster                                                     |
| coroutines                 | 22.3 ms                                                                     | 22.2 ms: 1.00x faster                                                    |
| async_generators           | 441 ms                                                                      | 445 ms: 1.01x slower                                                     |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 106 ms                                                                      | 101 ms: 1.05x faster                                                     |
| float          | 64.4 ms                                                                     | 63.6 ms: 1.01x faster                                                    |
| pidigits       | 255 ms                                                                      | 255 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.70 ms                                                                     | 3.65 ms: 1.01x faster                                                    |
| regex_compile  | 133 ms                                                                      | 133 ms: 1.01x faster                                                     |
| regex_v8       | 23.4 ms                                                                     | 23.3 ms: 1.00x faster                                                    |
| regex_dna      | 224 ms                                                                      | 227 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 80.8 ms                                                                     | 79.4 ms: 1.02x faster                                                    |
| pickle_pure_python   | 334 us                                                                      | 331 us: 1.01x faster                                                     |
| json_loads           | 25.5 us                                                                     | 25.3 us: 1.01x faster                                                    |
| unpickle_pure_python | 197 us                                                                      | 196 us: 1.01x faster                                                     |
| xml_etree_process    | 55.9 ms                                                                     | 55.7 ms: 1.00x faster                                                    |
| xml_etree_iterparse  | 97.3 ms                                                                     | 98.9 ms: 1.02x slower                                                    |
| xml_etree_parse      | 135 ms                                                                      | 141 ms: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                             |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                                     | 15.4 ms: 1.00x slower                                                    |
| python_startup_no_site | 8.85 ms                                                                     | 8.87 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                                     | 35.0 ms: 1.01x faster                                                    |
| mako            | 9.99 ms                                                                     | 9.94 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250707-pythonperf2-x86_64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coverage                   | 82.3 ms                                                                     | 77.9 ms: 1.06x faster                                                    |
| nbody                      | 106 ms                                                                      | 101 ms: 1.05x faster                                                     |
| pycparser                  | 1.26 sec                                                                    | 1.23 sec: 1.03x faster                                                   |
| typing_runtime_protocols   | 173 us                                                                      | 170 us: 1.02x faster                                                     |
| richards                   | 35.0 ms                                                                     | 34.4 ms: 1.02x faster                                                    |
| shortest_path              | 444 ms                                                                      | 437 ms: 1.02x faster                                                     |
| xml_etree_generate         | 80.8 ms                                                                     | 79.4 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 3.05 us                                                                     | 3.00 us: 1.02x faster                                                    |
| async_tree_memoization     | 335 ms                                                                      | 330 ms: 1.02x faster                                                     |
| nqueens                    | 94.6 ms                                                                     | 93.2 ms: 1.02x faster                                                    |
| django_template            | 35.5 ms                                                                     | 35.0 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.90 us                                                                     | 2.86 us: 1.01x faster                                                    |
| deepcopy                   | 283 us                                                                      | 279 us: 1.01x faster                                                     |
| dulwich_log                | 59.4 ms                                                                     | 58.6 ms: 1.01x faster                                                    |
| comprehensions             | 17.6 us                                                                     | 17.3 us: 1.01x faster                                                    |
| regex_effbot               | 3.70 ms                                                                     | 3.65 ms: 1.01x faster                                                    |
| float                      | 64.4 ms                                                                     | 63.6 ms: 1.01x faster                                                    |
| connected_components       | 409 ms                                                                      | 404 ms: 1.01x faster                                                     |
| scimark_sor                | 103 ms                                                                      | 102 ms: 1.01x faster                                                     |
| async_tree_io              | 632 ms                                                                      | 626 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.55 sec                                                                    | 1.54 sec: 1.01x faster                                                   |
| pickle_pure_python         | 334 us                                                                      | 331 us: 1.01x faster                                                     |
| json_loads                 | 25.5 us                                                                     | 25.3 us: 1.01x faster                                                    |
| async_tree_memoization_tg  | 335 ms                                                                      | 333 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 514 ms                                                                      | 510 ms: 1.01x faster                                                     |
| go                         | 129 ms                                                                      | 128 ms: 1.01x faster                                                     |
| deepcopy_memo              | 28.1 us                                                                     | 27.9 us: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 507 ms                                                                      | 503 ms: 1.01x faster                                                     |
| docutils                   | 2.93 sec                                                                    | 2.90 sec: 1.01x faster                                                   |
| unpickle_pure_python       | 197 us                                                                      | 196 us: 1.01x faster                                                     |
| mdp                        | 1.30 sec                                                                    | 1.29 sec: 1.01x faster                                                   |
| thrift                     | 842 us                                                                      | 837 us: 1.01x faster                                                     |
| crypto_pyaes               | 77.7 ms                                                                     | 77.3 ms: 1.01x faster                                                    |
| mako                       | 9.99 ms                                                                     | 9.94 ms: 1.01x faster                                                    |
| regex_compile              | 133 ms                                                                      | 133 ms: 1.01x faster                                                     |
| bpe_tokeniser              | 4.61 sec                                                                    | 4.59 sec: 1.00x faster                                                   |
| coroutines                 | 22.3 ms                                                                     | 22.2 ms: 1.00x faster                                                    |
| sympy_str                  | 292 ms                                                                      | 291 ms: 1.00x faster                                                     |
| regex_v8                   | 23.4 ms                                                                     | 23.3 ms: 1.00x faster                                                    |
| xml_etree_process          | 55.9 ms                                                                     | 55.7 ms: 1.00x faster                                                    |
| 2to3                       | 287 ms                                                                      | 287 ms: 1.00x faster                                                     |
| pidigits                   | 255 ms                                                                      | 255 ms: 1.00x slower                                                     |
| python_startup             | 15.4 ms                                                                     | 15.4 ms: 1.00x slower                                                    |
| sympy_integrate            | 22.4 ms                                                                     | 22.4 ms: 1.00x slower                                                    |
| python_startup_no_site     | 8.85 ms                                                                     | 8.87 ms: 1.00x slower                                                    |
| pathlib                    | 17.0 ms                                                                     | 17.1 ms: 1.00x slower                                                    |
| sqlglot_v2_optimize        | 57.9 ms                                                                     | 58.2 ms: 1.00x slower                                                    |
| sqlglot_v2_parse           | 1.33 ms                                                                     | 1.33 ms: 1.00x slower                                                    |
| subparsers                 | 25.2 ms                                                                     | 25.3 ms: 1.00x slower                                                    |
| scimark_lu                 | 95.7 ms                                                                     | 96.2 ms: 1.01x slower                                                    |
| sympy_expand               | 499 ms                                                                      | 502 ms: 1.01x slower                                                     |
| many_optionals             | 1.05 ms                                                                     | 1.06 ms: 1.01x slower                                                    |
| sqlglot_v2_normalize       | 116 ms                                                                      | 117 ms: 1.01x slower                                                     |
| async_generators           | 441 ms                                                                      | 445 ms: 1.01x slower                                                     |
| telco                      | 160 ms                                                                      | 161 ms: 1.01x slower                                                     |
| chaos                      | 59.5 ms                                                                     | 60.1 ms: 1.01x slower                                                    |
| json                       | 5.32 ms                                                                     | 5.37 ms: 1.01x slower                                                    |
| scimark_fft                | 309 ms                                                                      | 313 ms: 1.01x slower                                                     |
| regex_dna                  | 224 ms                                                                      | 227 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 5.11 ms                                                                     | 5.18 ms: 1.01x slower                                                    |
| create_gc_cycles           | 2.85 ms                                                                     | 2.90 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 97.3 ms                                                                     | 98.9 ms: 1.02x slower                                                    |
| logging_format             | 6.78 us                                                                     | 6.89 us: 1.02x slower                                                    |
| meteor_contest             | 121 ms                                                                      | 123 ms: 1.02x slower                                                     |
| fannkuch                   | 375 ms                                                                      | 384 ms: 1.02x slower                                                     |
| raytrace                   | 282 ms                                                                      | 289 ms: 1.02x slower                                                     |
| gc_traversal               | 6.30 ms                                                                     | 6.49 ms: 1.03x slower                                                    |
| spectral_norm              | 80.2 ms                                                                     | 83.0 ms: 1.03x slower                                                    |
| xml_etree_parse            | 135 ms                                                                      | 141 ms: 1.04x slower                                                     |
| pyflate                    | 404 ms                                                                      | 427 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (23): async_tree_none_tg, genshi_xml, genshi_text, html5lib, pylint, async_tree_none, richards_super, sympy_sum, sphinx, logging_silent, k_core, djangocms, deltablue, tomli_loads, hexiom, generators, json_dumps, scimark_monte_carlo, asyncio_websockets, async_tree_io_tg, sqlglot_v2_transpile, pprint_safe_repr, logging_simple

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 94.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x