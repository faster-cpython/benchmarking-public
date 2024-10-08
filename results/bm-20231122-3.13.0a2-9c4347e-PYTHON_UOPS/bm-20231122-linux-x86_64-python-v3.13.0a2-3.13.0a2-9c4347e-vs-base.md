# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                                               | 288 ms: 1.06x slower                                                                                             |
| chameleon      | 6.93 ms                                                                                              | 7.54 ms: 1.09x slower                                                                                            |
| docutils       | 2.69 sec                                                                                             | 2.73 sec: 1.01x slower                                                                                           |
| tornado_http   | 97.6 ms                                                                                              | 99.5 ms: 1.02x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.04x slower                                                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg | 1.26 sec                                                                                             | 1.25 sec: 1.01x faster                                                                                           |
| async_tree_io    | 1.22 sec                                                                                             | 1.22 sec: 1.00x faster                                                                                           |
| Geometric mean   | (ref)                                                                                                | 1.00x faster                                                                                                     |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                                               | 196 ms: 1.01x faster                                                                                             |
| float          | 83.5 ms                                                                                              | 92.4 ms: 1.11x slower                                                                                            |
| nbody          | 91.0 ms                                                                                              | 119 ms: 1.30x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.13x slower                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                                               | 224 ms: 1.02x slower                                                                                             |
| regex_v8       | 25.0 ms                                                                                              | 25.9 ms: 1.04x slower                                                                                            |
| regex_effbot   | 3.57 ms                                                                                              | 3.73 ms: 1.05x slower                                                                                            |
| regex_compile  | 137 ms                                                                                               | 157 ms: 1.15x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.06x slower                                                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pickle               | 11.8 us                                                                                              | 11.1 us: 1.06x faster                                                                                            |
| pickle_dict          | 34.9 us                                                                                              | 34.0 us: 1.03x faster                                                                                            |
| pickle_list          | 5.07 us                                                                                              | 4.94 us: 1.02x faster                                                                                            |
| xml_etree_parse      | 162 ms                                                                                               | 158 ms: 1.02x faster                                                                                             |
| pickle_pure_python   | 313 us                                                                                               | 308 us: 1.02x faster                                                                                             |
| json_loads           | 28.7 us                                                                                              | 28.2 us: 1.01x faster                                                                                            |
| unpickle             | 15.7 us                                                                                              | 15.6 us: 1.01x faster                                                                                            |
| json_dumps           | 10.7 ms                                                                                              | 10.6 ms: 1.01x faster                                                                                            |
| unpickle_list        | 5.12 us                                                                                              | 5.21 us: 1.02x slower                                                                                            |
| xml_etree_process    | 60.5 ms                                                                                              | 61.8 ms: 1.02x slower                                                                                            |
| xml_etree_generate   | 88.2 ms                                                                                              | 90.2 ms: 1.02x slower                                                                                            |
| xml_etree_iterparse  | 108 ms                                                                                               | 112 ms: 1.03x slower                                                                                             |
| unpickle_pure_python | 224 us                                                                                               | 240 us: 1.07x slower                                                                                             |
| tomli_loads          | 2.23 sec                                                                                             | 2.39 sec: 1.08x slower                                                                                           |
| Geometric mean       | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                                              | 10.3 ms: 1.03x faster                                                                                            |
| python_startup_no_site | 9.26 ms                                                                                              | 9.00 ms: 1.03x faster                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.03x faster                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mako      | 11.7 ms                                                                                              | 13.7 ms: 1.18x slower                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pickle                   | 11.8 us                                                                                              | 11.1 us: 1.06x faster                                                                                            |
| python_startup           | 10.7 ms                                                                                              | 10.3 ms: 1.03x faster                                                                                            |
| python_startup_no_site   | 9.26 ms                                                                                              | 9.00 ms: 1.03x faster                                                                                            |
| asyncio_tcp              | 501 ms                                                                                               | 487 ms: 1.03x faster                                                                                             |
| pickle_dict              | 34.9 us                                                                                              | 34.0 us: 1.03x faster                                                                                            |
| pickle_list              | 5.07 us                                                                                              | 4.94 us: 1.02x faster                                                                                            |
| xml_etree_parse          | 162 ms                                                                                               | 158 ms: 1.02x faster                                                                                             |
| asyncio_tcp_ssl          | 1.84 sec                                                                                             | 1.80 sec: 1.02x faster                                                                                           |
| asyncio_websockets       | 563 ms                                                                                               | 552 ms: 1.02x faster                                                                                             |
| gc_traversal             | 4.37 ms                                                                                              | 4.29 ms: 1.02x faster                                                                                            |
| create_gc_cycles         | 1.48 ms                                                                                              | 1.46 ms: 1.02x faster                                                                                            |
| generators               | 30.1 ms                                                                                              | 29.6 ms: 1.02x faster                                                                                            |
| pickle_pure_python       | 313 us                                                                                               | 308 us: 1.02x faster                                                                                             |
| json_loads               | 28.7 us                                                                                              | 28.2 us: 1.01x faster                                                                                            |
| logging_silent           | 109 ns                                                                                               | 108 ns: 1.01x faster                                                                                             |
| pidigits                 | 197 ms                                                                                               | 196 ms: 1.01x faster                                                                                             |
| async_tree_io_tg         | 1.26 sec                                                                                             | 1.25 sec: 1.01x faster                                                                                           |
| unpickle                 | 15.7 us                                                                                              | 15.6 us: 1.01x faster                                                                                            |
| json_dumps               | 10.7 ms                                                                                              | 10.6 ms: 1.01x faster                                                                                            |
| async_tree_io            | 1.22 sec                                                                                             | 1.22 sec: 1.00x faster                                                                                           |
| deepcopy_reduce          | 3.14 us                                                                                              | 3.18 us: 1.01x slower                                                                                            |
| sqlite_synth             | 2.87 us                                                                                              | 2.91 us: 1.01x slower                                                                                            |
| docutils                 | 2.69 sec                                                                                             | 2.73 sec: 1.01x slower                                                                                           |
| unpickle_list            | 5.12 us                                                                                              | 5.21 us: 1.02x slower                                                                                            |
| tornado_http             | 97.6 ms                                                                                              | 99.5 ms: 1.02x slower                                                                                            |
| regex_dna                | 219 ms                                                                                               | 224 ms: 1.02x slower                                                                                             |
| dulwich_log              | 67.6 ms                                                                                              | 69.0 ms: 1.02x slower                                                                                            |
| xml_etree_process        | 60.5 ms                                                                                              | 61.8 ms: 1.02x slower                                                                                            |
| pathlib                  | 18.6 ms                                                                                              | 19.0 ms: 1.02x slower                                                                                            |
| xml_etree_generate       | 88.2 ms                                                                                              | 90.2 ms: 1.02x slower                                                                                            |
| deepcopy                 | 354 us                                                                                               | 362 us: 1.02x slower                                                                                             |
| logging_simple           | 5.89 us                                                                                              | 6.03 us: 1.02x slower                                                                                            |
| scimark_lu               | 117 ms                                                                                               | 120 ms: 1.03x slower                                                                                             |
| typing_runtime_protocols | 119 us                                                                                               | 122 us: 1.03x slower                                                                                             |
| deepcopy_memo            | 39.8 us                                                                                              | 41.0 us: 1.03x slower                                                                                            |
| xml_etree_iterparse      | 108 ms                                                                                               | 112 ms: 1.03x slower                                                                                             |
| coroutines               | 21.8 ms                                                                                              | 22.4 ms: 1.03x slower                                                                                            |
| regex_v8                 | 25.0 ms                                                                                              | 25.9 ms: 1.04x slower                                                                                            |
| sqlglot_transpile        | 1.64 ms                                                                                              | 1.70 ms: 1.04x slower                                                                                            |
| sqlglot_parse            | 1.31 ms                                                                                              | 1.36 ms: 1.04x slower                                                                                            |
| richards_super           | 55.1 ms                                                                                              | 57.2 ms: 1.04x slower                                                                                            |
| regex_effbot             | 3.57 ms                                                                                              | 3.73 ms: 1.05x slower                                                                                            |
| meteor_contest           | 110 ms                                                                                               | 116 ms: 1.05x slower                                                                                             |
| sympy_sum                | 151 ms                                                                                               | 160 ms: 1.05x slower                                                                                             |
| logging_format           | 6.50 us                                                                                              | 6.86 us: 1.05x slower                                                                                            |
| mdp                      | 2.64 sec                                                                                             | 2.79 sec: 1.06x slower                                                                                           |
| pycparser                | 1.19 sec                                                                                             | 1.26 sec: 1.06x slower                                                                                           |
| 2to3                     | 272 ms                                                                                               | 288 ms: 1.06x slower                                                                                             |
| scimark_sor              | 126 ms                                                                                               | 134 ms: 1.06x slower                                                                                             |
| sympy_integrate          | 20.0 ms                                                                                              | 21.3 ms: 1.06x slower                                                                                            |
| sympy_expand             | 459 ms                                                                                               | 493 ms: 1.07x slower                                                                                             |
| unpickle_pure_python     | 224 us                                                                                               | 240 us: 1.07x slower                                                                                             |
| pprint_safe_repr         | 753 ms                                                                                               | 809 ms: 1.07x slower                                                                                             |
| pyflate                  | 484 ms                                                                                               | 521 ms: 1.07x slower                                                                                             |
| tomli_loads              | 2.23 sec                                                                                             | 2.39 sec: 1.08x slower                                                                                           |
| sqlglot_optimize         | 54.3 ms                                                                                              | 58.5 ms: 1.08x slower                                                                                            |
| sqlglot_normalize        | 107 ms                                                                                               | 115 ms: 1.08x slower                                                                                             |
| sympy_str                | 273 ms                                                                                               | 294 ms: 1.08x slower                                                                                             |
| chameleon                | 6.93 ms                                                                                              | 7.54 ms: 1.09x slower                                                                                            |
| raytrace                 | 284 ms                                                                                               | 310 ms: 1.09x slower                                                                                             |
| pprint_pformat           | 1.54 sec                                                                                             | 1.68 sec: 1.09x slower                                                                                           |
| float                    | 83.5 ms                                                                                              | 92.4 ms: 1.11x slower                                                                                            |
| go                       | 148 ms                                                                                               | 163 ms: 1.11x slower                                                                                             |
| fannkuch                 | 402 ms                                                                                               | 450 ms: 1.12x slower                                                                                             |
| scimark_sparse_mat_mult  | 5.13 ms                                                                                              | 5.74 ms: 1.12x slower                                                                                            |
| nqueens                  | 83.5 ms                                                                                              | 94.1 ms: 1.13x slower                                                                                            |
| crypto_pyaes             | 73.3 ms                                                                                              | 83.3 ms: 1.14x slower                                                                                            |
| regex_compile            | 137 ms                                                                                               | 157 ms: 1.15x slower                                                                                             |
| scimark_monte_carlo      | 70.0 ms                                                                                              | 81.4 ms: 1.16x slower                                                                                            |
| scimark_fft              | 375 ms                                                                                               | 436 ms: 1.16x slower                                                                                             |
| chaos                    | 63.4 ms                                                                                              | 74.2 ms: 1.17x slower                                                                                            |
| mako                     | 11.7 ms                                                                                              | 13.7 ms: 1.18x slower                                                                                            |
| comprehensions           | 17.0 us                                                                                              | 20.9 us: 1.22x slower                                                                                            |
| spectral_norm            | 111 ms                                                                                               | 140 ms: 1.27x slower                                                                                             |
| nbody                    | 91.0 ms                                                                                              | 119 ms: 1.30x slower                                                                                             |
| hexiom                   | 6.32 ms                                                                                              | 8.49 ms: 1.34x slower                                                                                            |
| deltablue                | 3.44 ms                                                                                              | 4.67 ms: 1.36x slower                                                                                            |
| Geometric mean           | (ref)                                                                                                | 1.05x slower                                                                                                     |

Benchmark hidden because not significant (14): async_tree_memoization_tg, telco, async_generators, async_tree_cpu_io_mixed, json, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, bench_thread_pool, mypy2, bench_mp_pool, richards, coverage, async_tree_none
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x