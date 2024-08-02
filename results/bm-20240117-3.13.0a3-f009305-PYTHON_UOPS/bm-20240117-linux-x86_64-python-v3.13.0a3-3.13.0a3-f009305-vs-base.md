# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                                               | 282 ms: 1.04x slower                                                                                             |
| chameleon      | 6.87 ms                                                                                              | 7.24 ms: 1.05x slower                                                                                            |
| docutils       | 2.68 sec                                                                                             | 2.71 sec: 1.01x slower                                                                                           |
| tornado_http   | 96.8 ms                                                                                              | 97.8 ms: 1.01x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_io    | 1.21 sec                                                                                             | 1.20 sec: 1.01x faster                                                                                           |
| async_tree_io_tg | 1.21 sec                                                                                             | 1.21 sec: 1.00x faster                                                                                           |
| Geometric mean   | (ref)                                                                                                | 1.00x faster                                                                                                     |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                                               | 190 ms: 1.01x faster                                                                                             |
| float          | 82.0 ms                                                                                              | 94.1 ms: 1.15x slower                                                                                            |
| nbody          | 89.5 ms                                                                                              | 119 ms: 1.33x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.15x slower                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                                              | 24.6 ms: 1.03x faster                                                                                            |
| regex_dna      | 230 ms                                                                                               | 228 ms: 1.01x faster                                                                                             |
| regex_effbot   | 3.68 ms                                                                                              | 3.74 ms: 1.02x slower                                                                                            |
| regex_compile  | 131 ms                                                                                               | 153 ms: 1.17x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 5.25 us                                                                                              | 5.14 us: 1.02x faster                                                                                            |
| json_loads           | 28.7 us                                                                                              | 28.2 us: 1.02x faster                                                                                            |
| xml_etree_parse      | 161 ms                                                                                               | 159 ms: 1.01x faster                                                                                             |
| xml_etree_process    | 59.9 ms                                                                                              | 61.1 ms: 1.02x slower                                                                                            |
| xml_etree_generate   | 87.4 ms                                                                                              | 89.5 ms: 1.02x slower                                                                                            |
| pickle               | 11.5 us                                                                                              | 11.8 us: 1.03x slower                                                                                            |
| pickle_dict          | 33.8 us                                                                                              | 35.0 us: 1.04x slower                                                                                            |
| pickle_list          | 4.98 us                                                                                              | 5.24 us: 1.05x slower                                                                                            |
| xml_etree_iterparse  | 106 ms                                                                                               | 112 ms: 1.05x slower                                                                                             |
| unpickle_pure_python | 218 us                                                                                               | 234 us: 1.07x slower                                                                                             |
| tomli_loads          | 2.16 sec                                                                                             | 2.61 sec: 1.21x slower                                                                                           |
| Geometric mean       | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmark hidden because not significant (3): pickle_pure_python, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.4 ms                                                                                              | 10.1 ms: 1.03x faster                                                                                            |
| python_startup_no_site | 8.92 ms                                                                                              | 8.72 ms: 1.02x faster                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.03x faster                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mako      | 11.3 ms                                                                                              | 14.2 ms: 1.26x slower                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| json                     | 5.39 ms                                                                                              | 5.19 ms: 1.04x faster                                                                                            |
| regex_v8                 | 25.4 ms                                                                                              | 24.6 ms: 1.03x faster                                                                                            |
| logging_silent           | 105 ns                                                                                               | 102 ns: 1.03x faster                                                                                             |
| python_startup           | 10.4 ms                                                                                              | 10.1 ms: 1.03x faster                                                                                            |
| gc_traversal             | 3.78 ms                                                                                              | 3.69 ms: 1.03x faster                                                                                            |
| python_startup_no_site   | 8.92 ms                                                                                              | 8.72 ms: 1.02x faster                                                                                            |
| unpickle_list            | 5.25 us                                                                                              | 5.14 us: 1.02x faster                                                                                            |
| asyncio_websockets       | 563 ms                                                                                               | 551 ms: 1.02x faster                                                                                             |
| json_loads               | 28.7 us                                                                                              | 28.2 us: 1.02x faster                                                                                            |
| create_gc_cycles         | 1.51 ms                                                                                              | 1.49 ms: 1.02x faster                                                                                            |
| pathlib                  | 18.5 ms                                                                                              | 18.3 ms: 1.01x faster                                                                                            |
| richards                 | 48.9 ms                                                                                              | 48.3 ms: 1.01x faster                                                                                            |
| asyncio_tcp_ssl          | 1.83 sec                                                                                             | 1.81 sec: 1.01x faster                                                                                           |
| xml_etree_parse          | 161 ms                                                                                               | 159 ms: 1.01x faster                                                                                             |
| regex_dna                | 230 ms                                                                                               | 228 ms: 1.01x faster                                                                                             |
| coverage                 | 95.8 ms                                                                                              | 95.0 ms: 1.01x faster                                                                                            |
| richards_super           | 55.1 ms                                                                                              | 54.7 ms: 1.01x faster                                                                                            |
| pidigits                 | 191 ms                                                                                               | 190 ms: 1.01x faster                                                                                             |
| async_tree_io            | 1.21 sec                                                                                             | 1.20 sec: 1.01x faster                                                                                           |
| async_tree_io_tg         | 1.21 sec                                                                                             | 1.21 sec: 1.00x faster                                                                                           |
| generators               | 29.2 ms                                                                                              | 29.3 ms: 1.01x slower                                                                                            |
| bench_thread_pool        | 842 us                                                                                               | 848 us: 1.01x slower                                                                                             |
| bench_mp_pool            | 23.8 ms                                                                                              | 24.0 ms: 1.01x slower                                                                                            |
| sqlite_synth             | 2.88 us                                                                                              | 2.91 us: 1.01x slower                                                                                            |
| tornado_http             | 96.8 ms                                                                                              | 97.8 ms: 1.01x slower                                                                                            |
| docutils                 | 2.68 sec                                                                                             | 2.71 sec: 1.01x slower                                                                                           |
| deepcopy_reduce          | 3.11 us                                                                                              | 3.15 us: 1.01x slower                                                                                            |
| async_generators         | 454 ms                                                                                               | 461 ms: 1.02x slower                                                                                             |
| regex_effbot             | 3.68 ms                                                                                              | 3.74 ms: 1.02x slower                                                                                            |
| coroutines               | 22.3 ms                                                                                              | 22.7 ms: 1.02x slower                                                                                            |
| scimark_sor              | 131 ms                                                                                               | 134 ms: 1.02x slower                                                                                             |
| xml_etree_process        | 59.9 ms                                                                                              | 61.1 ms: 1.02x slower                                                                                            |
| xml_etree_generate       | 87.4 ms                                                                                              | 89.5 ms: 1.02x slower                                                                                            |
| deepcopy                 | 350 us                                                                                               | 359 us: 1.02x slower                                                                                             |
| pickle                   | 11.5 us                                                                                              | 11.8 us: 1.03x slower                                                                                            |
| dulwich_log              | 66.8 ms                                                                                              | 69.0 ms: 1.03x slower                                                                                            |
| mdp                      | 2.58 sec                                                                                             | 2.67 sec: 1.03x slower                                                                                           |
| pickle_dict              | 33.8 us                                                                                              | 35.0 us: 1.04x slower                                                                                            |
| meteor_contest           | 110 ms                                                                                               | 114 ms: 1.04x slower                                                                                             |
| sqlglot_transpile        | 1.61 ms                                                                                              | 1.67 ms: 1.04x slower                                                                                            |
| 2to3                     | 270 ms                                                                                               | 282 ms: 1.04x slower                                                                                             |
| sqlglot_parse            | 1.28 ms                                                                                              | 1.34 ms: 1.05x slower                                                                                            |
| scimark_lu               | 114 ms                                                                                               | 119 ms: 1.05x slower                                                                                             |
| pickle_list              | 4.98 us                                                                                              | 5.24 us: 1.05x slower                                                                                            |
| logging_simple           | 5.89 us                                                                                              | 6.20 us: 1.05x slower                                                                                            |
| xml_etree_iterparse      | 106 ms                                                                                               | 112 ms: 1.05x slower                                                                                             |
| chameleon                | 6.87 ms                                                                                              | 7.24 ms: 1.05x slower                                                                                            |
| sympy_integrate          | 20.0 ms                                                                                              | 21.1 ms: 1.06x slower                                                                                            |
| typing_runtime_protocols | 110 us                                                                                               | 117 us: 1.06x slower                                                                                             |
| deepcopy_memo            | 38.4 us                                                                                              | 40.8 us: 1.06x slower                                                                                            |
| sympy_sum                | 152 ms                                                                                               | 161 ms: 1.06x slower                                                                                             |
| sympy_expand             | 466 ms                                                                                               | 495 ms: 1.06x slower                                                                                             |
| sqlglot_normalize        | 109 ms                                                                                               | 116 ms: 1.06x slower                                                                                             |
| sqlglot_optimize         | 54.8 ms                                                                                              | 58.4 ms: 1.07x slower                                                                                            |
| unpickle_pure_python     | 218 us                                                                                               | 234 us: 1.07x slower                                                                                             |
| logging_format           | 6.53 us                                                                                              | 7.07 us: 1.08x slower                                                                                            |
| pprint_safe_repr         | 745 ms                                                                                               | 816 ms: 1.10x slower                                                                                             |
| sympy_str                | 275 ms                                                                                               | 302 ms: 1.10x slower                                                                                             |
| pprint_pformat           | 1.53 sec                                                                                             | 1.70 sec: 1.11x slower                                                                                           |
| go                       | 140 ms                                                                                               | 156 ms: 1.11x slower                                                                                             |
| fannkuch                 | 402 ms                                                                                               | 454 ms: 1.13x slower                                                                                             |
| pyflate                  | 471 ms                                                                                               | 536 ms: 1.14x slower                                                                                             |
| raytrace                 | 264 ms                                                                                               | 302 ms: 1.14x slower                                                                                             |
| float                    | 82.0 ms                                                                                              | 94.1 ms: 1.15x slower                                                                                            |
| regex_compile            | 131 ms                                                                                               | 153 ms: 1.17x slower                                                                                             |
| crypto_pyaes             | 72.3 ms                                                                                              | 85.0 ms: 1.18x slower                                                                                            |
| nqueens                  | 80.7 ms                                                                                              | 95.4 ms: 1.18x slower                                                                                            |
| scimark_monte_carlo      | 68.6 ms                                                                                              | 81.4 ms: 1.19x slower                                                                                            |
| tomli_loads              | 2.16 sec                                                                                             | 2.61 sec: 1.21x slower                                                                                           |
| chaos                    | 59.9 ms                                                                                              | 73.6 ms: 1.23x slower                                                                                            |
| scimark_sparse_mat_mult  | 5.10 ms                                                                                              | 6.38 ms: 1.25x slower                                                                                            |
| scimark_fft              | 366 ms                                                                                               | 457 ms: 1.25x slower                                                                                             |
| mako                     | 11.3 ms                                                                                              | 14.2 ms: 1.26x slower                                                                                            |
| nbody                    | 89.5 ms                                                                                              | 119 ms: 1.33x slower                                                                                             |
| comprehensions           | 16.3 us                                                                                              | 21.6 us: 1.33x slower                                                                                            |
| spectral_norm            | 111 ms                                                                                               | 154 ms: 1.39x slower                                                                                             |
| hexiom                   | 6.10 ms                                                                                              | 8.65 ms: 1.42x slower                                                                                            |
| deltablue                | 3.23 ms                                                                                              | 4.85 ms: 1.50x slower                                                                                            |
| Geometric mean           | (ref)                                                                                                | 1.06x slower                                                                                                     |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pickle_pure_python, asyncio_tcp, mypy2, async_tree_memoization, async_tree_memoization_tg, pycparser, async_tree_none_tg, json_dumps, async_tree_none, telco, unpickle
Ignored benchmarks (10) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x