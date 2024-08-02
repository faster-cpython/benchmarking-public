# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                                                                   | 261 ms: 1.01x faster                                                                                                         |
| docutils       | 1.96 sec                                                                                                                 | 1.98 sec: 1.01x slower                                                                                                       |
| html5lib       | 51.4 ms                                                                                                                  | 47.7 ms: 1.08x faster                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.02x faster                                                                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io              | 570 ms                                                                                                                   | 546 ms: 1.05x faster                                                                                                         |
| async_tree_io_tg           | 528 ms                                                                                                                   | 506 ms: 1.04x faster                                                                                                         |
| async_tree_none_tg         | 204 ms                                                                                                                   | 197 ms: 1.03x faster                                                                                                         |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                                                                   | 458 ms: 1.03x faster                                                                                                         |
| async_tree_cpu_io_mixed    | 484 ms                                                                                                                   | 479 ms: 1.01x faster                                                                                                         |
| asyncio_tcp_ssl            | 17.2 sec                                                                                                                 | 17.1 sec: 1.01x faster                                                                                                       |
| async_generators           | 306 ms                                                                                                                   | 320 ms: 1.04x slower                                                                                                         |
| Geometric mean             | (ref)                                                                                                                    | 1.01x faster                                                                                                                 |

Benchmark hidden because not significant (5): async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                                                                   | 52.6 ms: 1.93x faster                                                                                                        |
| float          | 61.5 ms                                                                                                                  | 42.5 ms: 1.45x faster                                                                                                        |
| pidigits       | 200 ms                                                                                                                   | 196 ms: 1.02x faster                                                                                                         |
| Geometric mean | (ref)                                                                                                                    | 1.42x faster                                                                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 111 ms                                                                                                                   | 96.1 ms: 1.16x faster                                                                                                        |
| regex_dna      | 129 ms                                                                                                                   | 120 ms: 1.07x faster                                                                                                         |
| regex_effbot   | 2.05 ms                                                                                                                  | 2.00 ms: 1.02x faster                                                                                                        |
| regex_v8       | 16.4 ms                                                                                                                  | 16.1 ms: 1.02x faster                                                                                                        |
| Geometric mean | (ref)                                                                                                                    | 1.07x faster                                                                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| pickle_pure_python   | 266 us                                                                                                                   | 213 us: 1.25x faster                                                                                                         |
| tomli_loads          | 1.91 sec                                                                                                                 | 1.54 sec: 1.24x faster                                                                                                       |
| unpickle_pure_python | 174 us                                                                                                                   | 147 us: 1.18x faster                                                                                                         |
| xml_etree_generate   | 65.8 ms                                                                                                                  | 59.6 ms: 1.10x faster                                                                                                        |
| json_dumps           | 7.71 ms                                                                                                                  | 7.05 ms: 1.09x faster                                                                                                        |
| xml_etree_process    | 49.1 ms                                                                                                                  | 44.9 ms: 1.09x faster                                                                                                        |
| xml_etree_iterparse  | 67.7 ms                                                                                                                  | 63.9 ms: 1.06x faster                                                                                                        |
| xml_etree_parse      | 105 ms                                                                                                                   | 107 ms: 1.01x slower                                                                                                         |
| json_loads           | 20.8 us                                                                                                                  | 21.1 us: 1.02x slower                                                                                                        |
| Geometric mean       | (ref)                                                                                                                    | 1.11x faster                                                                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 23.7 ms                                                                                                                  | 24.8 ms: 1.04x slower                                                                                                        |
| python_startup_no_site | 19.6 ms                                                                                                                  | 20.8 ms: 1.06x slower                                                                                                        |
| Geometric mean         | (ref)                                                                                                                    | 1.05x slower                                                                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|-----------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| mako            | 8.31 ms                                                                                                                  | 5.43 ms: 1.53x faster                                                                                                        |
| django_template | 34.9 ms                                                                                                                  | 32.8 ms: 1.06x faster                                                                                                        |
| genshi_xml      | 50.4 ms                                                                                                                  | 53.5 ms: 1.06x slower                                                                                                        |
| Geometric mean  | (ref)                                                                                                                    | 1.11x faster                                                                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json | results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json |
|----------------------------|:------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 102 ms                                                                                                                   | 52.6 ms: 1.93x faster                                                                                                        |
| spectral_norm              | 78.0 ms                                                                                                                  | 47.9 ms: 1.63x faster                                                                                                        |
| mako                       | 8.31 ms                                                                                                                  | 5.43 ms: 1.53x faster                                                                                                        |
| scimark_sor                | 101 ms                                                                                                                   | 67.0 ms: 1.50x faster                                                                                                        |
| float                      | 61.5 ms                                                                                                                  | 42.5 ms: 1.45x faster                                                                                                        |
| fannkuch                   | 325 ms                                                                                                                   | 227 ms: 1.44x faster                                                                                                         |
| deepcopy_memo              | 23.0 us                                                                                                                  | 16.4 us: 1.40x faster                                                                                                        |
| scimark_fft                | 235 ms                                                                                                                   | 168 ms: 1.40x faster                                                                                                         |
| scimark_monte_carlo        | 58.2 ms                                                                                                                  | 41.8 ms: 1.39x faster                                                                                                        |
| scimark_sparse_mat_mult    | 3.17 ms                                                                                                                  | 2.32 ms: 1.37x faster                                                                                                        |
| pyflate                    | 360 ms                                                                                                                   | 269 ms: 1.34x faster                                                                                                         |
| logging_silent             | 75.3 ns                                                                                                                  | 58.2 ns: 1.29x faster                                                                                                        |
| crypto_pyaes               | 59.8 ms                                                                                                                  | 46.9 ms: 1.27x faster                                                                                                        |
| pickle_pure_python         | 266 us                                                                                                                   | 213 us: 1.25x faster                                                                                                         |
| richards                   | 43.7 ms                                                                                                                  | 35.1 ms: 1.25x faster                                                                                                        |
| tomli_loads                | 1.91 sec                                                                                                                 | 1.54 sec: 1.24x faster                                                                                                       |
| comprehensions             | 14.1 us                                                                                                                  | 11.5 us: 1.22x faster                                                                                                        |
| meteor_contest             | 83.9 ms                                                                                                                  | 69.0 ms: 1.22x faster                                                                                                        |
| scimark_lu                 | 72.4 ms                                                                                                                  | 59.7 ms: 1.21x faster                                                                                                        |
| unpickle_pure_python       | 174 us                                                                                                                   | 147 us: 1.18x faster                                                                                                         |
| pprint_safe_repr           | 685 ms                                                                                                                   | 586 ms: 1.17x faster                                                                                                         |
| pprint_pformat             | 1.39 sec                                                                                                                 | 1.20 sec: 1.16x faster                                                                                                       |
| regex_compile              | 111 ms                                                                                                                   | 96.1 ms: 1.16x faster                                                                                                        |
| pycparser                  | 918 ms                                                                                                                   | 793 ms: 1.16x faster                                                                                                         |
| sqlglot_parse              | 1.12 ms                                                                                                                  | 973 us: 1.15x faster                                                                                                         |
| richards_super             | 47.4 ms                                                                                                                  | 41.7 ms: 1.14x faster                                                                                                        |
| generators                 | 27.9 ms                                                                                                                  | 24.7 ms: 1.13x faster                                                                                                        |
| hexiom                     | 5.40 ms                                                                                                                  | 4.84 ms: 1.12x faster                                                                                                        |
| sqlglot_transpile          | 1.38 ms                                                                                                                  | 1.25 ms: 1.11x faster                                                                                                        |
| xml_etree_generate         | 65.8 ms                                                                                                                  | 59.6 ms: 1.10x faster                                                                                                        |
| telco                      | 6.60 ms                                                                                                                  | 6.01 ms: 1.10x faster                                                                                                        |
| json_dumps                 | 7.71 ms                                                                                                                  | 7.05 ms: 1.09x faster                                                                                                        |
| xml_etree_process          | 49.1 ms                                                                                                                  | 44.9 ms: 1.09x faster                                                                                                        |
| logging_simple             | 8.27 us                                                                                                                  | 7.62 us: 1.09x faster                                                                                                        |
| html5lib                   | 51.4 ms                                                                                                                  | 47.7 ms: 1.08x faster                                                                                                        |
| go                         | 124 ms                                                                                                                   | 115 ms: 1.08x faster                                                                                                         |
| logging_format             | 8.98 us                                                                                                                  | 8.36 us: 1.07x faster                                                                                                        |
| regex_dna                  | 129 ms                                                                                                                   | 120 ms: 1.07x faster                                                                                                         |
| django_template            | 34.9 ms                                                                                                                  | 32.8 ms: 1.06x faster                                                                                                        |
| raytrace                   | 241 ms                                                                                                                   | 227 ms: 1.06x faster                                                                                                         |
| xml_etree_iterparse        | 67.7 ms                                                                                                                  | 63.9 ms: 1.06x faster                                                                                                        |
| chaos                      | 54.7 ms                                                                                                                  | 51.6 ms: 1.06x faster                                                                                                        |
| deepcopy_reduce            | 2.66 us                                                                                                                  | 2.54 us: 1.05x faster                                                                                                        |
| async_tree_io              | 570 ms                                                                                                                   | 546 ms: 1.05x faster                                                                                                         |
| async_tree_io_tg           | 528 ms                                                                                                                   | 506 ms: 1.04x faster                                                                                                         |
| deepcopy                   | 264 us                                                                                                                   | 254 us: 1.04x faster                                                                                                         |
| mdp                        | 1.76 sec                                                                                                                 | 1.69 sec: 1.04x faster                                                                                                       |
| async_tree_none_tg         | 204 ms                                                                                                                   | 197 ms: 1.03x faster                                                                                                         |
| deltablue                  | 2.84 ms                                                                                                                  | 2.75 ms: 1.03x faster                                                                                                        |
| async_tree_cpu_io_mixed_tg | 472 ms                                                                                                                   | 458 ms: 1.03x faster                                                                                                         |
| dulwich_log                | 51.6 ms                                                                                                                  | 50.2 ms: 1.03x faster                                                                                                        |
| nqueens                    | 79.0 ms                                                                                                                  | 77.2 ms: 1.02x faster                                                                                                        |
| regex_effbot               | 2.05 ms                                                                                                                  | 2.00 ms: 1.02x faster                                                                                                        |
| pidigits                   | 200 ms                                                                                                                   | 196 ms: 1.02x faster                                                                                                         |
| regex_v8                   | 16.4 ms                                                                                                                  | 16.1 ms: 1.02x faster                                                                                                        |
| sympy_str                  | 225 ms                                                                                                                   | 222 ms: 1.02x faster                                                                                                         |
| 2to3                       | 264 ms                                                                                                                   | 261 ms: 1.01x faster                                                                                                         |
| async_tree_cpu_io_mixed    | 484 ms                                                                                                                   | 479 ms: 1.01x faster                                                                                                         |
| coverage                   | 52.2 ms                                                                                                                  | 51.8 ms: 1.01x faster                                                                                                        |
| asyncio_tcp_ssl            | 17.2 sec                                                                                                                 | 17.1 sec: 1.01x faster                                                                                                       |
| sympy_expand               | 392 ms                                                                                                                   | 394 ms: 1.00x slower                                                                                                         |
| sqlglot_optimize           | 44.6 ms                                                                                                                  | 44.9 ms: 1.01x slower                                                                                                        |
| docutils                   | 1.96 sec                                                                                                                 | 1.98 sec: 1.01x slower                                                                                                       |
| gc_traversal               | 1.44 ms                                                                                                                  | 1.46 ms: 1.01x slower                                                                                                        |
| sqlglot_normalize          | 229 ms                                                                                                                   | 232 ms: 1.01x slower                                                                                                         |
| xml_etree_parse            | 105 ms                                                                                                                   | 107 ms: 1.01x slower                                                                                                         |
| json_loads                 | 20.8 us                                                                                                                  | 21.1 us: 1.02x slower                                                                                                        |
| create_gc_cycles           | 753 us                                                                                                                   | 771 us: 1.02x slower                                                                                                         |
| sympy_integrate            | 16.1 ms                                                                                                                  | 16.6 ms: 1.03x slower                                                                                                        |
| thrift                     | 751 us                                                                                                                   | 774 us: 1.03x slower                                                                                                         |
| bench_mp_pool              | 74.2 ms                                                                                                                  | 77.3 ms: 1.04x slower                                                                                                        |
| async_generators           | 306 ms                                                                                                                   | 320 ms: 1.04x slower                                                                                                         |
| python_startup             | 23.7 ms                                                                                                                  | 24.8 ms: 1.04x slower                                                                                                        |
| python_startup_no_site     | 19.6 ms                                                                                                                  | 20.8 ms: 1.06x slower                                                                                                        |
| genshi_xml                 | 50.4 ms                                                                                                                  | 53.5 ms: 1.06x slower                                                                                                        |
| pylint                     | 239 ms                                                                                                                   | 257 ms: 1.07x slower                                                                                                         |
| Geometric mean             | (ref)                                                                                                                    | 1.10x faster                                                                                                                 |

Benchmark hidden because not significant (12): async_tree_none, async_tree_memoization_tg, pathlib, asyncio_tcp, sympy_sum, tornado_http, genshi_text, async_tree_memoization, coroutines, typing_runtime_protocols, bench_thread_pool, json

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown