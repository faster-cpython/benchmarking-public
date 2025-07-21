# Results vs. base

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                                                                     | 219 ms: 1.01x faster                                                                                                           |
| docutils       | 1.62 sec                                                                                                                   | 1.65 sec: 1.01x slower                                                                                                         |
| Geometric mean | (ref)                                                                                                                      | 1.00x faster                                                                                                                   |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets      | 168 ms                                                                                                                     | 160 ms: 1.05x faster                                                                                                           |
| async_tree_none_tg      | 170 ms                                                                                                                     | 167 ms: 1.02x faster                                                                                                           |
| async_tree_none         | 170 ms                                                                                                                     | 168 ms: 1.01x faster                                                                                                           |
| coroutines              | 14.4 ms                                                                                                                    | 14.2 ms: 1.01x faster                                                                                                          |
| async_tree_cpu_io_mixed | 328 ms                                                                                                                     | 332 ms: 1.01x slower                                                                                                           |
| async_generators        | 233 ms                                                                                                                     | 248 ms: 1.06x slower                                                                                                           |
| asyncio_tcp_ssl         | 1.29 sec                                                                                                                   | 1.42 sec: 1.10x slower                                                                                                         |
| asyncio_tcp             | 398 ms                                                                                                                     | 506 ms: 1.27x slower                                                                                                           |
| Geometric mean          | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.2 ms                                                                                                                    | 57.3 ms: 1.12x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                                                                    | 13.8 ms: 1.03x faster                                                                                                          |
| regex_dna      | 120 ms                                                                                                                     | 116 ms: 1.03x faster                                                                                                           |
| regex_compile  | 79.9 ms                                                                                                                    | 78.6 ms: 1.02x faster                                                                                                          |
| regex_effbot   | 1.57 ms                                                                                                                    | 1.54 ms: 1.02x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                                                                     | 105 us: 1.29x faster                                                                                                           |
| tomli_loads          | 1.41 sec                                                                                                                   | 1.11 sec: 1.27x faster                                                                                                         |
| xml_etree_generate   | 55.9 ms                                                                                                                    | 51.0 ms: 1.10x faster                                                                                                          |
| xml_etree_process    | 38.5 ms                                                                                                                    | 35.3 ms: 1.09x faster                                                                                                          |
| pickle               | 8.26 us                                                                                                                    | 7.59 us: 1.09x faster                                                                                                          |
| pickle_pure_python   | 213 us                                                                                                                     | 203 us: 1.05x faster                                                                                                           |
| unpickle_list        | 2.86 us                                                                                                                    | 2.77 us: 1.03x faster                                                                                                          |
| pickle_list          | 3.39 us                                                                                                                    | 3.29 us: 1.03x faster                                                                                                          |
| pickle_dict          | 19.9 us                                                                                                                    | 19.4 us: 1.03x faster                                                                                                          |
| json_dumps           | 6.31 ms                                                                                                                    | 6.18 ms: 1.02x faster                                                                                                          |
| xml_etree_parse      | 86.8 ms                                                                                                                    | 87.3 ms: 1.01x slower                                                                                                          |
| json_loads           | 14.1 us                                                                                                                    | 14.4 us: 1.03x slower                                                                                                          |
| unpickle             | 8.42 us                                                                                                                    | 8.68 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.53 ms                                                                                                                    | 5.42 ms: 1.20x faster                                                                                                          |
| genshi_text    | 15.1 ms                                                                                                                    | 15.5 ms: 1.02x slower                                                                                                          |
| genshi_xml     | 34.0 ms                                                                                                                    | 34.8 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python     | 135 us                                                                                                                     | 105 us: 1.29x faster                                                                                                           |
| scimark_fft              | 189 ms                                                                                                                     | 149 ms: 1.27x faster                                                                                                           |
| tomli_loads              | 1.41 sec                                                                                                                   | 1.11 sec: 1.27x faster                                                                                                         |
| fannkuch                 | 269 ms                                                                                                                     | 213 ms: 1.26x faster                                                                                                           |
| mako                     | 6.53 ms                                                                                                                    | 5.42 ms: 1.20x faster                                                                                                          |
| pyflate                  | 289 ms                                                                                                                     | 251 ms: 1.15x faster                                                                                                           |
| pprint_safe_repr         | 508 ms                                                                                                                     | 443 ms: 1.15x faster                                                                                                           |
| pprint_pformat           | 1.02 sec                                                                                                                   | 897 ms: 1.14x faster                                                                                                           |
| bpe_tokeniser            | 2.92 sec                                                                                                                   | 2.58 sec: 1.13x faster                                                                                                         |
| nbody                    | 64.2 ms                                                                                                                    | 57.3 ms: 1.12x faster                                                                                                          |
| scimark_sparse_mat_mult  | 2.50 ms                                                                                                                    | 2.23 ms: 1.12x faster                                                                                                          |
| xml_etree_generate       | 55.9 ms                                                                                                                    | 51.0 ms: 1.10x faster                                                                                                          |
| xml_etree_process        | 38.5 ms                                                                                                                    | 35.3 ms: 1.09x faster                                                                                                          |
| pickle                   | 8.26 us                                                                                                                    | 7.59 us: 1.09x faster                                                                                                          |
| telco                    | 4.60 ms                                                                                                                    | 4.29 ms: 1.07x faster                                                                                                          |
| crypto_pyaes             | 48.4 ms                                                                                                                    | 45.6 ms: 1.06x faster                                                                                                          |
| k_core                   | 1.70 sec                                                                                                                   | 1.61 sec: 1.06x faster                                                                                                         |
| meteor_contest           | 72.6 ms                                                                                                                    | 69.1 ms: 1.05x faster                                                                                                          |
| asyncio_websockets       | 168 ms                                                                                                                     | 160 ms: 1.05x faster                                                                                                           |
| pickle_pure_python       | 213 us                                                                                                                     | 203 us: 1.05x faster                                                                                                           |
| sqlglot_v2_parse         | 815 us                                                                                                                     | 781 us: 1.04x faster                                                                                                           |
| typing_runtime_protocols | 105 us                                                                                                                     | 101 us: 1.04x faster                                                                                                           |
| coverage                 | 51.8 ms                                                                                                                    | 49.7 ms: 1.04x faster                                                                                                          |
| richards                 | 27.8 ms                                                                                                                    | 26.8 ms: 1.04x faster                                                                                                          |
| richards_super           | 31.9 ms                                                                                                                    | 30.8 ms: 1.04x faster                                                                                                          |
| pycparser                | 714 ms                                                                                                                     | 689 ms: 1.04x faster                                                                                                           |
| thrift                   | 505 us                                                                                                                     | 488 us: 1.04x faster                                                                                                           |
| regex_v8                 | 14.3 ms                                                                                                                    | 13.8 ms: 1.03x faster                                                                                                          |
| raytrace                 | 184 ms                                                                                                                     | 178 ms: 1.03x faster                                                                                                           |
| regex_dna                | 120 ms                                                                                                                     | 116 ms: 1.03x faster                                                                                                           |
| unpickle_list            | 2.86 us                                                                                                                    | 2.77 us: 1.03x faster                                                                                                          |
| pickle_list              | 3.39 us                                                                                                                    | 3.29 us: 1.03x faster                                                                                                          |
| connected_components     | 332 ms                                                                                                                     | 321 ms: 1.03x faster                                                                                                           |
| pickle_dict              | 19.9 us                                                                                                                    | 19.4 us: 1.03x faster                                                                                                          |
| sqlglot_v2_transpile     | 1.02 ms                                                                                                                    | 987 us: 1.03x faster                                                                                                           |
| logging_silent           | 55.6 ns                                                                                                                    | 54.1 ns: 1.03x faster                                                                                                          |
| logging_format           | 6.75 us                                                                                                                    | 6.57 us: 1.03x faster                                                                                                          |
| logging_simple           | 6.29 us                                                                                                                    | 6.14 us: 1.03x faster                                                                                                          |
| spectral_norm            | 64.5 ms                                                                                                                    | 63.1 ms: 1.02x faster                                                                                                          |
| comprehensions           | 10.7 us                                                                                                                    | 10.5 us: 1.02x faster                                                                                                          |
| json_dumps               | 6.31 ms                                                                                                                    | 6.18 ms: 1.02x faster                                                                                                          |
| nqueens                  | 62.2 ms                                                                                                                    | 61.1 ms: 1.02x faster                                                                                                          |
| shortest_path            | 361 ms                                                                                                                     | 354 ms: 1.02x faster                                                                                                           |
| deepcopy_memo            | 18.3 us                                                                                                                    | 18.0 us: 1.02x faster                                                                                                          |
| regex_compile            | 79.9 ms                                                                                                                    | 78.6 ms: 1.02x faster                                                                                                          |
| async_tree_none_tg       | 170 ms                                                                                                                     | 167 ms: 1.02x faster                                                                                                           |
| scimark_sor              | 79.2 ms                                                                                                                    | 78.0 ms: 1.02x faster                                                                                                          |
| regex_effbot             | 1.57 ms                                                                                                                    | 1.54 ms: 1.02x faster                                                                                                          |
| async_tree_none          | 170 ms                                                                                                                     | 168 ms: 1.01x faster                                                                                                           |
| sqlglot_v2_normalize     | 71.0 ms                                                                                                                    | 70.1 ms: 1.01x faster                                                                                                          |
| deepcopy                 | 171 us                                                                                                                     | 170 us: 1.01x faster                                                                                                           |
| chaos                    | 41.0 ms                                                                                                                    | 40.6 ms: 1.01x faster                                                                                                          |
| mdp                      | 804 ms                                                                                                                     | 796 ms: 1.01x faster                                                                                                           |
| deltablue                | 2.21 ms                                                                                                                    | 2.19 ms: 1.01x faster                                                                                                          |
| create_gc_cycles         | 1.30 ms                                                                                                                    | 1.29 ms: 1.01x faster                                                                                                          |
| 2to3                     | 221 ms                                                                                                                     | 219 ms: 1.01x faster                                                                                                           |
| coroutines               | 14.4 ms                                                                                                                    | 14.2 ms: 1.01x faster                                                                                                          |
| go                       | 77.1 ms                                                                                                                    | 76.7 ms: 1.01x faster                                                                                                          |
| xml_etree_parse          | 86.8 ms                                                                                                                    | 87.3 ms: 1.01x slower                                                                                                          |
| sqlglot_v2_optimize      | 34.0 ms                                                                                                                    | 34.2 ms: 1.01x slower                                                                                                          |
| sympy_str                | 169 ms                                                                                                                     | 171 ms: 1.01x slower                                                                                                           |
| async_tree_cpu_io_mixed  | 328 ms                                                                                                                     | 332 ms: 1.01x slower                                                                                                           |
| sympy_expand             | 289 ms                                                                                                                     | 293 ms: 1.01x slower                                                                                                           |
| docutils                 | 1.62 sec                                                                                                                   | 1.65 sec: 1.01x slower                                                                                                         |
| many_optionals           | 439 us                                                                                                                     | 446 us: 1.02x slower                                                                                                           |
| sympy_integrate          | 12.4 ms                                                                                                                    | 12.6 ms: 1.02x slower                                                                                                          |
| generators               | 19.3 ms                                                                                                                    | 19.6 ms: 1.02x slower                                                                                                          |
| genshi_text              | 15.1 ms                                                                                                                    | 15.5 ms: 1.02x slower                                                                                                          |
| genshi_xml               | 34.0 ms                                                                                                                    | 34.8 ms: 1.02x slower                                                                                                          |
| json_loads               | 14.1 us                                                                                                                    | 14.4 us: 1.03x slower                                                                                                          |
| scimark_monte_carlo      | 40.4 ms                                                                                                                    | 41.5 ms: 1.03x slower                                                                                                          |
| unpickle                 | 8.42 us                                                                                                                    | 8.68 us: 1.03x slower                                                                                                          |
| json                     | 2.88 ms                                                                                                                    | 3.01 ms: 1.05x slower                                                                                                          |
| unpack_sequence          | 32.6 ns                                                                                                                    | 34.5 ns: 1.06x slower                                                                                                          |
| async_generators         | 233 ms                                                                                                                     | 248 ms: 1.06x slower                                                                                                           |
| scimark_lu               | 58.6 ms                                                                                                                    | 63.8 ms: 1.09x slower                                                                                                          |
| asyncio_tcp_ssl          | 1.29 sec                                                                                                                   | 1.42 sec: 1.10x slower                                                                                                         |
| asyncio_tcp              | 398 ms                                                                                                                     | 506 ms: 1.27x slower                                                                                                           |
| Geometric mean           | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (24): html5lib, async_tree_io_tg, pathlib, async_tree_memoization_tg, python_startup_no_site, sphinx, async_tree_memoization, float, pidigits, dulwich_log, gc_traversal, bench_thread_pool, deepcopy_reduce, async_tree_cpu_io_mixed_tg, sympy_sum, sqlite_synth, async_tree_io, hexiom, python_startup, subparsers, django_template, xml_etree_iterparse, bench_mp_pool, pylint

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown