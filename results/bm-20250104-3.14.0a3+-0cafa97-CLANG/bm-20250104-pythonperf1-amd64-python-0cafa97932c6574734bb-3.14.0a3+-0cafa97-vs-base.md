# Results vs. base

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.032x slower
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                                                                 | 235 ms: 1.05x slower                                                                                                         |
| docutils       | 1.65 sec                                                                                                               | 1.76 sec: 1.07x slower                                                                                                       |
| sphinx         | 645 ms                                                                                                                 | 697 ms: 1.08x slower                                                                                                         |
| Geometric mean | (ref)                                                                                                                  | 1.05x slower                                                                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 396 ms                                                                                                                 | 382 ms: 1.04x faster                                                                                                         |
| async_tree_none_tg         | 170 ms                                                                                                                 | 164 ms: 1.03x faster                                                                                                         |
| async_tree_memoization     | 222 ms                                                                                                                 | 215 ms: 1.03x faster                                                                                                         |
| async_tree_none            | 179 ms                                                                                                                 | 174 ms: 1.03x faster                                                                                                         |
| async_tree_memoization_tg  | 211 ms                                                                                                                 | 205 ms: 1.03x faster                                                                                                         |
| async_tree_io              | 397 ms                                                                                                                 | 388 ms: 1.02x faster                                                                                                         |
| coroutines                 | 13.4 ms                                                                                                                | 13.7 ms: 1.02x slower                                                                                                        |
| async_generators           | 237 ms                                                                                                                 | 251 ms: 1.06x slower                                                                                                         |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                                                                 | 368 ms: 1.08x slower                                                                                                         |
| async_tree_cpu_io_mixed    | 345 ms                                                                                                                 | 372 ms: 1.08x slower                                                                                                         |
| Geometric mean             | (ref)                                                                                                                  | 1.00x slower                                                                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 75.3 ms                                                                                                                | 67.5 ms: 1.12x faster                                                                                                        |
| float          | 52.1 ms                                                                                                                | 52.8 ms: 1.01x slower                                                                                                        |
| pidigits       | 148 ms                                                                                                                 | 156 ms: 1.05x slower                                                                                                         |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 86.5 ms                                                                                                                | 87.9 ms: 1.02x slower                                                                                                        |
| regex_dna      | 116 ms                                                                                                                 | 130 ms: 1.11x slower                                                                                                         |
| regex_effbot   | 1.46 ms                                                                                                                | 1.88 ms: 1.29x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                  | 1.12x slower                                                                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                                                                               | 1.38 sec: 1.01x faster                                                                                                       |
| pickle_pure_python   | 220 us                                                                                                                 | 222 us: 1.01x slower                                                                                                         |
| unpickle_pure_python | 145 us                                                                                                                 | 154 us: 1.06x slower                                                                                                         |
| xml_etree_iterparse  | 62.5 ms                                                                                                                | 69.5 ms: 1.11x slower                                                                                                        |
| xml_etree_process    | 39.6 ms                                                                                                                | 45.7 ms: 1.15x slower                                                                                                        |
| xml_etree_parse      | 88.8 ms                                                                                                                | 103 ms: 1.16x slower                                                                                                         |
| xml_etree_generate   | 56.4 ms                                                                                                                | 66.0 ms: 1.17x slower                                                                                                        |
| json_dumps           | 6.57 ms                                                                                                                | 7.84 ms: 1.19x slower                                                                                                        |
| json_loads           | 14.1 us                                                                                                                | 19.3 us: 1.37x slower                                                                                                        |
| Geometric mean       | (ref)                                                                                                                  | 1.13x slower                                                                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.3 ms                                                                                                                | 18.6 ms: 1.08x slower                                                                                                        |
| python_startup         | 23.6 ms                                                                                                                | 25.6 ms: 1.09x slower                                                                                                        |
| Geometric mean         | (ref)                                                                                                                  | 1.08x slower                                                                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 17.5 ms                                                                                                                | 16.0 ms: 1.09x faster                                                                                                        |
| genshi_xml      | 36.2 ms                                                                                                                | 34.2 ms: 1.06x faster                                                                                                        |
| django_template | 25.5 ms                                                                                                                | 24.8 ms: 1.03x faster                                                                                                        |
| mako            | 6.69 ms                                                                                                                | 8.22 ms: 1.23x slower                                                                                                        |
| Geometric mean  | (ref)                                                                                                                  | 1.01x slower                                                                                                                 |

All benchmarks:
===============

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| generators                 | 21.2 ms                                                                                                                | 17.2 ms: 1.23x faster                                                                                                        |
| deltablue                  | 2.25 ms                                                                                                                | 2.02 ms: 1.12x faster                                                                                                        |
| nbody                      | 75.3 ms                                                                                                                | 67.5 ms: 1.12x faster                                                                                                        |
| go                         | 87.1 ms                                                                                                                | 78.2 ms: 1.11x faster                                                                                                        |
| genshi_text                | 17.5 ms                                                                                                                | 16.0 ms: 1.09x faster                                                                                                        |
| scimark_sor                | 86.1 ms                                                                                                                | 79.2 ms: 1.09x faster                                                                                                        |
| raytrace                   | 190 ms                                                                                                                 | 177 ms: 1.07x faster                                                                                                         |
| sqlglot_parse              | 895 us                                                                                                                 | 845 us: 1.06x faster                                                                                                         |
| genshi_xml                 | 36.2 ms                                                                                                                | 34.2 ms: 1.06x faster                                                                                                        |
| meteor_contest             | 76.9 ms                                                                                                                | 73.6 ms: 1.05x faster                                                                                                        |
| scimark_monte_carlo        | 45.8 ms                                                                                                                | 44.0 ms: 1.04x faster                                                                                                        |
| sqlglot_transpile          | 1.11 ms                                                                                                                | 1.07 ms: 1.04x faster                                                                                                        |
| async_tree_io_tg           | 396 ms                                                                                                                 | 382 ms: 1.04x faster                                                                                                         |
| async_tree_none_tg         | 170 ms                                                                                                                 | 164 ms: 1.03x faster                                                                                                         |
| async_tree_memoization     | 222 ms                                                                                                                 | 215 ms: 1.03x faster                                                                                                         |
| async_tree_none            | 179 ms                                                                                                                 | 174 ms: 1.03x faster                                                                                                         |
| async_tree_memoization_tg  | 211 ms                                                                                                                 | 205 ms: 1.03x faster                                                                                                         |
| logging_format             | 6.86 us                                                                                                                | 6.68 us: 1.03x faster                                                                                                        |
| django_template            | 25.5 ms                                                                                                                | 24.8 ms: 1.03x faster                                                                                                        |
| logging_simple             | 6.36 us                                                                                                                | 6.20 us: 1.03x faster                                                                                                        |
| async_tree_io              | 397 ms                                                                                                                 | 388 ms: 1.02x faster                                                                                                         |
| richards_super             | 34.5 ms                                                                                                                | 33.9 ms: 1.02x faster                                                                                                        |
| richards                   | 30.4 ms                                                                                                                | 30.1 ms: 1.01x faster                                                                                                        |
| tomli_loads                | 1.39 sec                                                                                                               | 1.38 sec: 1.01x faster                                                                                                       |
| deepcopy                   | 185 us                                                                                                                 | 184 us: 1.01x faster                                                                                                         |
| pprint_safe_repr           | 531 ms                                                                                                                 | 529 ms: 1.00x faster                                                                                                         |
| hexiom                     | 4.34 ms                                                                                                                | 4.37 ms: 1.01x slower                                                                                                        |
| sympy_expand               | 306 ms                                                                                                                 | 308 ms: 1.01x slower                                                                                                         |
| scimark_fft                | 193 ms                                                                                                                 | 195 ms: 1.01x slower                                                                                                         |
| pickle_pure_python         | 220 us                                                                                                                 | 222 us: 1.01x slower                                                                                                         |
| sympy_integrate            | 13.3 ms                                                                                                                | 13.5 ms: 1.01x slower                                                                                                        |
| scimark_sparse_mat_mult    | 2.59 ms                                                                                                                | 2.63 ms: 1.01x slower                                                                                                        |
| sqlglot_normalize          | 195 ms                                                                                                                 | 197 ms: 1.01x slower                                                                                                         |
| connected_components       | 322 ms                                                                                                                 | 326 ms: 1.01x slower                                                                                                         |
| float                      | 52.1 ms                                                                                                                | 52.8 ms: 1.01x slower                                                                                                        |
| subparsers                 | 16.0 ms                                                                                                                | 16.2 ms: 1.02x slower                                                                                                        |
| sympy_str                  | 178 ms                                                                                                                 | 180 ms: 1.02x slower                                                                                                         |
| regex_compile              | 86.5 ms                                                                                                                | 87.9 ms: 1.02x slower                                                                                                        |
| coroutines                 | 13.4 ms                                                                                                                | 13.7 ms: 1.02x slower                                                                                                        |
| sympy_sum                  | 89.9 ms                                                                                                                | 91.5 ms: 1.02x slower                                                                                                        |
| typing_runtime_protocols   | 113 us                                                                                                                 | 115 us: 1.02x slower                                                                                                         |
| sqlglot_optimize           | 35.9 ms                                                                                                                | 36.6 ms: 1.02x slower                                                                                                        |
| chaos                      | 43.0 ms                                                                                                                | 43.9 ms: 1.02x slower                                                                                                        |
| many_optionals             | 443 us                                                                                                                 | 454 us: 1.03x slower                                                                                                         |
| deepcopy_reduce            | 1.88 us                                                                                                                | 1.93 us: 1.03x slower                                                                                                        |
| pylint                     | 198 ms                                                                                                                 | 205 ms: 1.03x slower                                                                                                         |
| 2to3                       | 224 ms                                                                                                                 | 235 ms: 1.05x slower                                                                                                         |
| deepcopy_memo              | 19.8 us                                                                                                                | 20.7 us: 1.05x slower                                                                                                        |
| fannkuch                   | 270 ms                                                                                                                 | 283 ms: 1.05x slower                                                                                                         |
| pathlib                    | 75.8 ms                                                                                                                | 79.6 ms: 1.05x slower                                                                                                        |
| pidigits                   | 148 ms                                                                                                                 | 156 ms: 1.05x slower                                                                                                         |
| thrift                     | 533 us                                                                                                                 | 561 us: 1.05x slower                                                                                                         |
| comprehensions             | 11.8 us                                                                                                                | 12.5 us: 1.05x slower                                                                                                        |
| async_generators           | 237 ms                                                                                                                 | 251 ms: 1.06x slower                                                                                                         |
| unpickle_pure_python       | 145 us                                                                                                                 | 154 us: 1.06x slower                                                                                                         |
| docutils                   | 1.65 sec                                                                                                               | 1.76 sec: 1.07x slower                                                                                                       |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                                                                 | 368 ms: 1.08x slower                                                                                                         |
| python_startup_no_site     | 17.3 ms                                                                                                                | 18.6 ms: 1.08x slower                                                                                                        |
| async_tree_cpu_io_mixed    | 345 ms                                                                                                                 | 372 ms: 1.08x slower                                                                                                         |
| sphinx                     | 645 ms                                                                                                                 | 697 ms: 1.08x slower                                                                                                         |
| sqlite_synth               | 1.61 us                                                                                                                | 1.75 us: 1.09x slower                                                                                                        |
| python_startup             | 23.6 ms                                                                                                                | 25.6 ms: 1.09x slower                                                                                                        |
| logging_silent             | 61.6 ns                                                                                                                | 67.3 ns: 1.09x slower                                                                                                        |
| coverage                   | 45.8 ms                                                                                                                | 50.1 ms: 1.10x slower                                                                                                        |
| bpe_tokeniser              | 3.00 sec                                                                                                               | 3.30 sec: 1.10x slower                                                                                                       |
| telco                      | 4.76 ms                                                                                                                | 5.24 ms: 1.10x slower                                                                                                        |
| spectral_norm              | 62.2 ms                                                                                                                | 68.9 ms: 1.11x slower                                                                                                        |
| xml_etree_iterparse        | 62.5 ms                                                                                                                | 69.5 ms: 1.11x slower                                                                                                        |
| regex_dna                  | 116 ms                                                                                                                 | 130 ms: 1.11x slower                                                                                                         |
| scimark_lu                 | 60.5 ms                                                                                                                | 67.7 ms: 1.12x slower                                                                                                        |
| create_gc_cycles           | 1.20 ms                                                                                                                | 1.35 ms: 1.12x slower                                                                                                        |
| crypto_pyaes               | 48.1 ms                                                                                                                | 54.8 ms: 1.14x slower                                                                                                        |
| bench_mp_pool              | 82.3 ms                                                                                                                | 93.9 ms: 1.14x slower                                                                                                        |
| mdp                        | 1.46 sec                                                                                                               | 1.67 sec: 1.15x slower                                                                                                       |
| xml_etree_process          | 39.6 ms                                                                                                                | 45.7 ms: 1.15x slower                                                                                                        |
| xml_etree_parse            | 88.8 ms                                                                                                                | 103 ms: 1.16x slower                                                                                                         |
| xml_etree_generate         | 56.4 ms                                                                                                                | 66.0 ms: 1.17x slower                                                                                                        |
| json_dumps                 | 6.57 ms                                                                                                                | 7.84 ms: 1.19x slower                                                                                                        |
| json                       | 2.98 ms                                                                                                                | 3.61 ms: 1.21x slower                                                                                                        |
| mako                       | 6.69 ms                                                                                                                | 8.22 ms: 1.23x slower                                                                                                        |
| gc_traversal               | 1.98 ms                                                                                                                | 2.54 ms: 1.28x slower                                                                                                        |
| regex_effbot               | 1.46 ms                                                                                                                | 1.88 ms: 1.29x slower                                                                                                        |
| json_loads                 | 14.1 us                                                                                                                | 19.3 us: 1.37x slower                                                                                                        |
| Geometric mean             | (ref)                                                                                                                  | 1.04x slower                                                                                                                 |

Benchmark hidden because not significant (11): pyflate, html5lib, k_core, pprint_pformat, nqueens, shortest_path, dulwich_log, pycparser, asyncio_websockets, bench_thread_pool, regex_v8
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: mypy2

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 99.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown