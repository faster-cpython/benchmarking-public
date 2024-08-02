# Results vs. base

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.02x slower
- HPT reliability: 99.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                                                                               | 232 ms: 1.11x slower                                                                                                     |
| chameleon      | 4.74 ms                                                                                                              | 4.99 ms: 1.05x slower                                                                                                    |
| docutils       | 1.62 sec                                                                                                             | 1.76 sec: 1.09x slower                                                                                                   |
| html5lib       | 34.1 ms                                                                                                              | 37.0 ms: 1.08x slower                                                                                                    |
| tornado_http   | 82.5 ms                                                                                                              | 85.4 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.07x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 607 ms                                                                                                               | 619 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed | 386 ms                                                                                                               | 396 ms: 1.03x slower                                                                                                     |
| async_tree_none         | 220 ms                                                                                                               | 226 ms: 1.03x slower                                                                                                     |
| async_tree_memoization  | 267 ms                                                                                                               | 275 ms: 1.03x slower                                                                                                     |
| async_tree_none_tg      | 206 ms                                                                                                               | 213 ms: 1.03x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                                                                              | 49.9 ms: 1.37x faster                                                                                                    |
| float          | 48.8 ms                                                                                                              | 43.4 ms: 1.12x faster                                                                                                    |
| pidigits       | 150 ms                                                                                                               | 150 ms: 1.00x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.16x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.63 ms                                                                                                              | 1.56 ms: 1.05x faster                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 114 ms: 1.04x faster                                                                                                     |
| regex_compile  | 77.4 ms                                                                                                              | 86.6 ms: 1.12x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.38 sec                                                                                                             | 1.23 sec: 1.13x faster                                                                                                   |
| pickle_list          | 3.11 us                                                                                                              | 2.80 us: 1.11x faster                                                                                                    |
| pickle_dict          | 18.3 us                                                                                                              | 17.5 us: 1.05x faster                                                                                                    |
| xml_etree_generate   | 52.7 ms                                                                                                              | 51.1 ms: 1.03x faster                                                                                                    |
| xml_etree_iterparse  | 61.5 ms                                                                                                              | 59.9 ms: 1.03x faster                                                                                                    |
| pickle_pure_python   | 177 us                                                                                                               | 172 us: 1.03x faster                                                                                                     |
| unpickle             | 8.88 us                                                                                                              | 8.69 us: 1.02x faster                                                                                                    |
| xml_etree_process    | 36.3 ms                                                                                                              | 36.1 ms: 1.01x faster                                                                                                    |
| xml_etree_parse      | 90.1 ms                                                                                                              | 91.6 ms: 1.02x slower                                                                                                    |
| unpickle_list        | 2.83 us                                                                                                              | 2.88 us: 1.02x slower                                                                                                    |
| json_loads           | 14.0 us                                                                                                              | 14.3 us: 1.02x slower                                                                                                    |
| json_dumps           | 5.53 ms                                                                                                              | 5.65 ms: 1.02x slower                                                                                                    |
| pickle               | 7.17 us                                                                                                              | 7.35 us: 1.02x slower                                                                                                    |
| unpickle_pure_python | 119 us                                                                                                               | 124 us: 1.04x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.1 ms                                                                                                              | 18.2 ms: 1.06x slower                                                                                                    |
| python_startup         | 20.5 ms                                                                                                              | 22.0 ms: 1.07x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.07x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.20 ms                                                                                                              | 4.94 ms: 1.26x faster                                                                                                    |
| django_template | 22.0 ms                                                                                                              | 25.4 ms: 1.15x slower                                                                                                    |
| genshi_text     | 14.7 ms                                                                                                              | 17.8 ms: 1.21x slower                                                                                                    |
| genshi_xml      | 32.1 ms                                                                                                              | 44.8 ms: 1.40x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.12x slower                                                                                                             |

All benchmarks:
===============

| Benchmark                | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 62.1 ms                                                                                                              | 44.9 ms: 1.38x faster                                                                                                    |
| nbody                    | 68.4 ms                                                                                                              | 49.9 ms: 1.37x faster                                                                                                    |
| mako                     | 6.20 ms                                                                                                              | 4.94 ms: 1.26x faster                                                                                                    |
| scimark_fft              | 182 ms                                                                                                               | 150 ms: 1.21x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.57 ms                                                                                                              | 2.14 ms: 1.20x faster                                                                                                    |
| crypto_pyaes             | 47.5 ms                                                                                                              | 40.8 ms: 1.17x faster                                                                                                    |
| tomli_loads              | 1.38 sec                                                                                                             | 1.23 sec: 1.13x faster                                                                                                   |
| fannkuch                 | 251 ms                                                                                                               | 223 ms: 1.12x faster                                                                                                     |
| float                    | 48.8 ms                                                                                                              | 43.4 ms: 1.12x faster                                                                                                    |
| pickle_list              | 3.11 us                                                                                                              | 2.80 us: 1.11x faster                                                                                                    |
| scimark_monte_carlo      | 41.7 ms                                                                                                              | 37.9 ms: 1.10x faster                                                                                                    |
| deepcopy_memo            | 22.3 us                                                                                                              | 20.5 us: 1.09x faster                                                                                                    |
| pyflate                  | 282 ms                                                                                                               | 262 ms: 1.08x faster                                                                                                     |
| pprint_safe_repr         | 471 ms                                                                                                               | 450 ms: 1.05x faster                                                                                                     |
| pickle_dict              | 18.3 us                                                                                                              | 17.5 us: 1.05x faster                                                                                                    |
| regex_effbot             | 1.63 ms                                                                                                              | 1.56 ms: 1.05x faster                                                                                                    |
| regex_dna                | 119 ms                                                                                                               | 114 ms: 1.04x faster                                                                                                     |
| pprint_pformat           | 963 ms                                                                                                               | 924 ms: 1.04x faster                                                                                                     |
| json                     | 3.13 ms                                                                                                              | 3.01 ms: 1.04x faster                                                                                                    |
| asyncio_tcp              | 564 ms                                                                                                               | 545 ms: 1.04x faster                                                                                                     |
| xml_etree_generate       | 52.7 ms                                                                                                              | 51.1 ms: 1.03x faster                                                                                                    |
| telco                    | 4.77 ms                                                                                                              | 4.63 ms: 1.03x faster                                                                                                    |
| xml_etree_iterparse      | 61.5 ms                                                                                                              | 59.9 ms: 1.03x faster                                                                                                    |
| pickle_pure_python       | 177 us                                                                                                               | 172 us: 1.03x faster                                                                                                     |
| sqlite_synth             | 1.62 us                                                                                                              | 1.58 us: 1.02x faster                                                                                                    |
| unpickle                 | 8.88 us                                                                                                              | 8.69 us: 1.02x faster                                                                                                    |
| xml_etree_process        | 36.3 ms                                                                                                              | 36.1 ms: 1.01x faster                                                                                                    |
| pidigits                 | 150 ms                                                                                                               | 150 ms: 1.00x faster                                                                                                     |
| logging_format           | 6.27 us                                                                                                              | 6.31 us: 1.01x slower                                                                                                    |
| logging_simple           | 5.82 us                                                                                                              | 5.88 us: 1.01x slower                                                                                                    |
| meteor_contest           | 72.4 ms                                                                                                              | 73.2 ms: 1.01x slower                                                                                                    |
| bench_mp_pool            | 69.7 ms                                                                                                              | 70.5 ms: 1.01x slower                                                                                                    |
| create_gc_cycles         | 892 us                                                                                                               | 906 us: 1.02x slower                                                                                                     |
| bench_thread_pool        | 818 us                                                                                                               | 832 us: 1.02x slower                                                                                                     |
| xml_etree_parse          | 90.1 ms                                                                                                              | 91.6 ms: 1.02x slower                                                                                                    |
| gc_traversal             | 1.54 ms                                                                                                              | 1.57 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg         | 607 ms                                                                                                               | 619 ms: 1.02x slower                                                                                                     |
| unpickle_list            | 2.83 us                                                                                                              | 2.88 us: 1.02x slower                                                                                                    |
| json_loads               | 14.0 us                                                                                                              | 14.3 us: 1.02x slower                                                                                                    |
| json_dumps               | 5.53 ms                                                                                                              | 5.65 ms: 1.02x slower                                                                                                    |
| pickle                   | 7.17 us                                                                                                              | 7.35 us: 1.02x slower                                                                                                    |
| async_tree_cpu_io_mixed  | 386 ms                                                                                                               | 396 ms: 1.03x slower                                                                                                     |
| async_tree_none          | 220 ms                                                                                                               | 226 ms: 1.03x slower                                                                                                     |
| logging_silent           | 52.9 ns                                                                                                              | 54.5 ns: 1.03x slower                                                                                                    |
| async_tree_memoization   | 267 ms                                                                                                               | 275 ms: 1.03x slower                                                                                                     |
| mdp                      | 1.43 sec                                                                                                             | 1.47 sec: 1.03x slower                                                                                                   |
| chaos                    | 38.3 ms                                                                                                              | 39.4 ms: 1.03x slower                                                                                                    |
| richards_super           | 31.3 ms                                                                                                              | 32.3 ms: 1.03x slower                                                                                                    |
| async_tree_none_tg       | 206 ms                                                                                                               | 213 ms: 1.03x slower                                                                                                     |
| richards                 | 27.5 ms                                                                                                              | 28.5 ms: 1.03x slower                                                                                                    |
| tornado_http             | 82.5 ms                                                                                                              | 85.4 ms: 1.04x slower                                                                                                    |
| deepcopy_reduce          | 1.96 us                                                                                                              | 2.04 us: 1.04x slower                                                                                                    |
| coverage                 | 43.2 ms                                                                                                              | 45.1 ms: 1.04x slower                                                                                                    |
| unpickle_pure_python     | 119 us                                                                                                               | 124 us: 1.04x slower                                                                                                     |
| coroutines               | 12.8 ms                                                                                                              | 13.3 ms: 1.05x slower                                                                                                    |
| sqlglot_parse            | 764 us                                                                                                               | 803 us: 1.05x slower                                                                                                     |
| chameleon                | 4.74 ms                                                                                                              | 4.99 ms: 1.05x slower                                                                                                    |
| python_startup_no_site   | 17.1 ms                                                                                                              | 18.2 ms: 1.06x slower                                                                                                    |
| nqueens                  | 57.4 ms                                                                                                              | 61.1 ms: 1.06x slower                                                                                                    |
| sqlglot_transpile        | 973 us                                                                                                               | 1.04 ms: 1.06x slower                                                                                                    |
| raytrace                 | 167 ms                                                                                                               | 179 ms: 1.07x slower                                                                                                     |
| deepcopy                 | 218 us                                                                                                               | 233 us: 1.07x slower                                                                                                     |
| python_startup           | 20.5 ms                                                                                                              | 22.0 ms: 1.07x slower                                                                                                    |
| pycparser                | 703 ms                                                                                                               | 754 ms: 1.07x slower                                                                                                     |
| thrift                   | 493 us                                                                                                               | 533 us: 1.08x slower                                                                                                     |
| html5lib                 | 34.1 ms                                                                                                              | 37.0 ms: 1.08x slower                                                                                                    |
| docutils                 | 1.62 sec                                                                                                             | 1.76 sec: 1.09x slower                                                                                                   |
| sympy_sum                | 84.9 ms                                                                                                              | 93.6 ms: 1.10x slower                                                                                                    |
| sympy_str                | 160 ms                                                                                                               | 178 ms: 1.11x slower                                                                                                     |
| 2to3                     | 209 ms                                                                                                               | 232 ms: 1.11x slower                                                                                                     |
| scimark_sor              | 74.1 ms                                                                                                              | 82.6 ms: 1.12x slower                                                                                                    |
| sqlglot_optimize         | 33.3 ms                                                                                                              | 37.1 ms: 1.12x slower                                                                                                    |
| regex_compile            | 77.4 ms                                                                                                              | 86.6 ms: 1.12x slower                                                                                                    |
| async_generators         | 230 ms                                                                                                               | 259 ms: 1.13x slower                                                                                                     |
| typing_runtime_protocols | 99.6 us                                                                                                              | 112 us: 1.13x slower                                                                                                     |
| sympy_expand             | 272 ms                                                                                                               | 309 ms: 1.14x slower                                                                                                     |
| go                       | 81.4 ms                                                                                                              | 92.6 ms: 1.14x slower                                                                                                    |
| generators               | 19.1 ms                                                                                                              | 22.0 ms: 1.15x slower                                                                                                    |
| sympy_integrate          | 12.2 ms                                                                                                              | 14.0 ms: 1.15x slower                                                                                                    |
| pylint                   | 206 ms                                                                                                               | 238 ms: 1.15x slower                                                                                                     |
| django_template          | 22.0 ms                                                                                                              | 25.4 ms: 1.15x slower                                                                                                    |
| genshi_text              | 14.7 ms                                                                                                              | 17.8 ms: 1.21x slower                                                                                                    |
| deltablue                | 1.92 ms                                                                                                              | 2.32 ms: 1.21x slower                                                                                                    |
| scimark_lu               | 55.1 ms                                                                                                              | 67.5 ms: 1.22x slower                                                                                                    |
| hexiom                   | 3.68 ms                                                                                                              | 4.65 ms: 1.26x slower                                                                                                    |
| genshi_xml               | 32.1 ms                                                                                                              | 44.8 ms: 1.40x slower                                                                                                    |
| Geometric mean           | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (8): regex_v8, comprehensions, pathlib, flaskblogging, async_tree_io, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: sqlglot_normalize

# HPT report

- Reliability score: 99.28% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown