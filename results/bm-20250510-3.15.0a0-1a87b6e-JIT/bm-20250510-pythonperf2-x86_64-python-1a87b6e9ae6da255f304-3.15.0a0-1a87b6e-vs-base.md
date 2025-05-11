# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.001x slower
- HPT reliability: 91.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 286 ms: 1.02x slower                                                                                                      |
| docutils       | 2.87 sec                                                                                                              | 2.93 sec: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io          | 629 ms                                                                                                                | 615 ms: 1.02x faster                                                                                                      |
| async_tree_memoization | 329 ms                                                                                                                | 326 ms: 1.01x faster                                                                                                      |
| asyncio_websockets     | 389 ms                                                                                                                | 385 ms: 1.01x faster                                                                                                      |
| asyncio_tcp_ssl        | 1.59 sec                                                                                                              | 1.58 sec: 1.00x faster                                                                                                    |
| coroutines             | 22.1 ms                                                                                                               | 22.3 ms: 1.01x slower                                                                                                     |
| async_generators       | 429 ms                                                                                                                | 446 ms: 1.04x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (3): async_tree_none, asyncio_tcp, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 70.1 ms                                                                                                               | 63.6 ms: 1.10x faster                                                                                                     |
| nbody          | 95.1 ms                                                                                                               | 96.5 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                                                                | 227 ms: 1.06x faster                                                                                                      |
| regex_v8       | 24.6 ms                                                                                                               | 23.7 ms: 1.04x faster                                                                                                     |
| regex_effbot   | 3.43 ms                                                                                                               | 3.33 ms: 1.03x faster                                                                                                     |
| regex_compile  | 134 ms                                                                                                                | 135 ms: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_process    | 58.8 ms                                                                                                               | 56.7 ms: 1.04x faster                                                                                                     |
| unpickle_pure_python | 215 us                                                                                                                | 208 us: 1.04x faster                                                                                                      |
| tomli_loads          | 2.09 sec                                                                                                              | 2.02 sec: 1.03x faster                                                                                                    |
| xml_etree_generate   | 85.0 ms                                                                                                               | 82.3 ms: 1.03x faster                                                                                                     |
| xml_etree_parse      | 141 ms                                                                                                                | 138 ms: 1.02x faster                                                                                                      |
| unpickle             | 14.4 us                                                                                                               | 14.5 us: 1.01x slower                                                                                                     |
| unpickle_list        | 4.91 us                                                                                                               | 5.00 us: 1.02x slower                                                                                                     |
| pickle_list          | 4.96 us                                                                                                               | 5.10 us: 1.03x slower                                                                                                     |
| pickle_dict          | 34.6 us                                                                                                               | 36.3 us: 1.05x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, json_dumps, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.77 ms                                                                                                               | 8.80 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                                                                               | 10.4 ms: 1.04x faster                                                                                                     |
| genshi_xml      | 53.3 ms                                                                                                               | 53.8 ms: 1.01x slower                                                                                                     |
| django_template | 35.8 ms                                                                                                               | 36.2 ms: 1.01x slower                                                                                                     |
| genshi_text     | 23.3 ms                                                                                                               | 23.6 ms: 1.01x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                 | 44.9 ms                                                                                                               | 37.4 ms: 1.20x faster                                                                                                     |
| richards_super           | 51.1 ms                                                                                                               | 42.8 ms: 1.19x faster                                                                                                     |
| float                    | 70.1 ms                                                                                                               | 63.6 ms: 1.10x faster                                                                                                     |
| coverage                 | 84.6 ms                                                                                                               | 79.6 ms: 1.06x faster                                                                                                     |
| regex_dna                | 240 ms                                                                                                                | 227 ms: 1.06x faster                                                                                                      |
| deltablue                | 3.13 ms                                                                                                               | 2.96 ms: 1.05x faster                                                                                                     |
| xml_etree_process        | 58.8 ms                                                                                                               | 56.7 ms: 1.04x faster                                                                                                     |
| regex_v8                 | 24.6 ms                                                                                                               | 23.7 ms: 1.04x faster                                                                                                     |
| mako                     | 10.8 ms                                                                                                               | 10.4 ms: 1.04x faster                                                                                                     |
| pycparser                | 1.27 sec                                                                                                              | 1.22 sec: 1.04x faster                                                                                                    |
| unpickle_pure_python     | 215 us                                                                                                                | 208 us: 1.04x faster                                                                                                      |
| tomli_loads              | 2.09 sec                                                                                                              | 2.02 sec: 1.03x faster                                                                                                    |
| xml_etree_generate       | 85.0 ms                                                                                                               | 82.3 ms: 1.03x faster                                                                                                     |
| regex_effbot             | 3.43 ms                                                                                                               | 3.33 ms: 1.03x faster                                                                                                     |
| async_tree_io            | 629 ms                                                                                                                | 615 ms: 1.02x faster                                                                                                      |
| deepcopy_reduce          | 2.96 us                                                                                                               | 2.90 us: 1.02x faster                                                                                                     |
| xml_etree_parse          | 141 ms                                                                                                                | 138 ms: 1.02x faster                                                                                                      |
| logging_silent           | 517 ns                                                                                                                | 507 ns: 1.02x faster                                                                                                      |
| logging_simple           | 6.59 us                                                                                                               | 6.49 us: 1.02x faster                                                                                                     |
| scimark_sor              | 105 ms                                                                                                                | 104 ms: 1.02x faster                                                                                                      |
| deepcopy                 | 278 us                                                                                                                | 274 us: 1.01x faster                                                                                                      |
| spectral_norm            | 92.6 ms                                                                                                               | 91.4 ms: 1.01x faster                                                                                                     |
| async_tree_memoization   | 329 ms                                                                                                                | 326 ms: 1.01x faster                                                                                                      |
| sqlite_synth             | 2.89 us                                                                                                               | 2.86 us: 1.01x faster                                                                                                     |
| bpe_tokeniser            | 4.68 sec                                                                                                              | 4.63 sec: 1.01x faster                                                                                                    |
| asyncio_websockets       | 389 ms                                                                                                                | 385 ms: 1.01x faster                                                                                                      |
| scimark_lu               | 95.2 ms                                                                                                               | 94.7 ms: 1.01x faster                                                                                                     |
| asyncio_tcp_ssl          | 1.59 sec                                                                                                              | 1.58 sec: 1.00x faster                                                                                                    |
| python_startup_no_site   | 8.77 ms                                                                                                               | 8.80 ms: 1.00x slower                                                                                                     |
| crypto_pyaes             | 79.8 ms                                                                                                               | 80.4 ms: 1.01x slower                                                                                                     |
| gc_traversal             | 6.42 ms                                                                                                               | 6.47 ms: 1.01x slower                                                                                                     |
| unpickle                 | 14.4 us                                                                                                               | 14.5 us: 1.01x slower                                                                                                     |
| regex_compile            | 134 ms                                                                                                                | 135 ms: 1.01x slower                                                                                                      |
| coroutines               | 22.1 ms                                                                                                               | 22.3 ms: 1.01x slower                                                                                                     |
| pyflate                  | 452 ms                                                                                                                | 456 ms: 1.01x slower                                                                                                      |
| genshi_xml               | 53.3 ms                                                                                                               | 53.8 ms: 1.01x slower                                                                                                     |
| generators               | 28.3 ms                                                                                                               | 28.5 ms: 1.01x slower                                                                                                     |
| mdp                      | 1.29 sec                                                                                                              | 1.31 sec: 1.01x slower                                                                                                    |
| django_template          | 35.8 ms                                                                                                               | 36.2 ms: 1.01x slower                                                                                                     |
| sympy_str                | 289 ms                                                                                                                | 292 ms: 1.01x slower                                                                                                      |
| genshi_text              | 23.3 ms                                                                                                               | 23.6 ms: 1.01x slower                                                                                                     |
| sympy_integrate          | 22.1 ms                                                                                                               | 22.4 ms: 1.01x slower                                                                                                     |
| nbody                    | 95.1 ms                                                                                                               | 96.5 ms: 1.01x slower                                                                                                     |
| 2to3                     | 281 ms                                                                                                                | 286 ms: 1.02x slower                                                                                                      |
| sympy_expand             | 497 ms                                                                                                                | 505 ms: 1.02x slower                                                                                                      |
| unpickle_list            | 4.91 us                                                                                                               | 5.00 us: 1.02x slower                                                                                                     |
| sqlglot_v2_transpile     | 1.70 ms                                                                                                               | 1.74 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_normalize     | 114 ms                                                                                                                | 116 ms: 1.02x slower                                                                                                      |
| many_optionals           | 1.02 ms                                                                                                               | 1.04 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_parse         | 1.32 ms                                                                                                               | 1.34 ms: 1.02x slower                                                                                                     |
| docutils                 | 2.87 sec                                                                                                              | 2.93 sec: 1.02x slower                                                                                                    |
| raytrace                 | 282 ms                                                                                                                | 288 ms: 1.02x slower                                                                                                      |
| scimark_fft              | 313 ms                                                                                                                | 319 ms: 1.02x slower                                                                                                      |
| chaos                    | 60.0 ms                                                                                                               | 61.4 ms: 1.02x slower                                                                                                     |
| deepcopy_memo            | 27.6 us                                                                                                               | 28.3 us: 1.03x slower                                                                                                     |
| pickle_list              | 4.96 us                                                                                                               | 5.10 us: 1.03x slower                                                                                                     |
| pprint_pformat           | 1.59 sec                                                                                                              | 1.63 sec: 1.03x slower                                                                                                    |
| sqlglot_v2_optimize      | 56.7 ms                                                                                                               | 58.4 ms: 1.03x slower                                                                                                     |
| thrift                   | 851 us                                                                                                                | 877 us: 1.03x slower                                                                                                      |
| typing_runtime_protocols | 171 us                                                                                                                | 177 us: 1.03x slower                                                                                                      |
| async_generators         | 429 ms                                                                                                                | 446 ms: 1.04x slower                                                                                                      |
| pprint_safe_repr         | 782 ms                                                                                                                | 815 ms: 1.04x slower                                                                                                      |
| meteor_contest           | 128 ms                                                                                                                | 134 ms: 1.04x slower                                                                                                      |
| pickle_dict              | 34.6 us                                                                                                               | 36.3 us: 1.05x slower                                                                                                     |
| scimark_sparse_mat_mult  | 4.75 ms                                                                                                               | 5.01 ms: 1.06x slower                                                                                                     |
| hexiom                   | 6.08 ms                                                                                                               | 6.57 ms: 1.08x slower                                                                                                     |
| go                       | 125 ms                                                                                                                | 138 ms: 1.11x slower                                                                                                      |
| scimark_monte_carlo      | 60.0 ms                                                                                                               | 66.7 ms: 1.11x slower                                                                                                     |
| fannkuch                 | 369 ms                                                                                                                | 412 ms: 1.12x slower                                                                                                      |
| comprehensions           | 17.1 us                                                                                                               | 19.2 us: 1.12x slower                                                                                                     |
| unpack_sequence          | 45.7 ns                                                                                                               | 63.3 ns: 1.38x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (24): bench_mp_pool, async_tree_none, subparsers, dulwich_log, json, xml_etree_iterparse, pathlib, djangocms, python_startup, pickle_pure_python, pidigits, json_dumps, html5lib, sympy_sum, asyncio_tcp, logging_format, bench_thread_pool, async_tree_cpu_io_mixed, json_loads, pylint, telco, pickle, create_gc_cycles, nqueens

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 91.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x