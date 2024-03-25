# Results vs. base

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                                                                                  | 302 ms: 1.04x slower                                                                                                        |
| chameleon      | 7.36 ms                                                                                                                 | 7.29 ms: 1.01x faster                                                                                                       |
| docutils       | 2.96 sec                                                                                                                | 3.04 sec: 1.03x slower                                                                                                      |
| html5lib       | 75.5 ms                                                                                                                 | 73.4 ms: 1.03x faster                                                                                                       |
| tornado_http   | 121 ms                                                                                                                  | 123 ms: 1.02x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io  | 851 ms                                                                                                                  | 860 ms: 1.01x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| float          | 78.2 ms                                                                                                                 | 76.2 ms: 1.03x faster                                                                                                       |
| nbody          | 86.8 ms                                                                                                                 | 100 ms: 1.15x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.04x slower                                                                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.70 ms                                                                                                                 | 3.47 ms: 1.07x faster                                                                                                       |
| regex_v8       | 25.6 ms                                                                                                                 | 25.7 ms: 1.01x slower                                                                                                       |
| regex_compile  | 144 ms                                                                                                                  | 145 ms: 1.01x slower                                                                                                        |
| regex_dna      | 233 ms                                                                                                                  | 249 ms: 1.07x slower                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.00x slower                                                                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.21 sec                                                                                                                | 2.14 sec: 1.03x faster                                                                                                      |
| xml_etree_parse      | 150 ms                                                                                                                  | 147 ms: 1.02x faster                                                                                                        |
| pickle_dict          | 30.9 us                                                                                                                 | 30.6 us: 1.01x faster                                                                                                       |
| xml_etree_iterparse  | 105 ms                                                                                                                  | 104 ms: 1.01x faster                                                                                                        |
| pickle               | 10.2 us                                                                                                                 | 10.2 us: 1.00x slower                                                                                                       |
| pickle_pure_python   | 307 us                                                                                                                  | 308 us: 1.00x slower                                                                                                        |
| json_dumps           | 10.5 ms                                                                                                                 | 10.6 ms: 1.01x slower                                                                                                       |
| json_loads           | 25.2 us                                                                                                                 | 25.4 us: 1.01x slower                                                                                                       |
| xml_etree_generate   | 82.0 ms                                                                                                                 | 82.9 ms: 1.01x slower                                                                                                       |
| xml_etree_process    | 57.8 ms                                                                                                                 | 58.6 ms: 1.01x slower                                                                                                       |
| pickle_list          | 4.37 us                                                                                                                 | 4.49 us: 1.03x slower                                                                                                       |
| unpickle_pure_python | 223 us                                                                                                                  | 230 us: 1.03x slower                                                                                                        |
| unpickle_list        | 4.47 us                                                                                                                 | 4.60 us: 1.03x slower                                                                                                       |
| unpickle             | 14.6 us                                                                                                                 | 15.1 us: 1.04x slower                                                                                                       |
| Geometric mean       | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                                                                 | 14.2 ms: 1.12x slower                                                                                                       |
| python_startup_no_site | 11.0 ms                                                                                                                 | 12.5 ms: 1.14x slower                                                                                                       |
| Geometric mean         | (ref)                                                                                                                   | 1.13x slower                                                                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                                                                 | 10.0 ms: 1.02x faster                                                                                                       |
| django_template | 40.9 ms                                                                                                                 | 40.4 ms: 1.01x faster                                                                                                       |
| genshi_xml      | 54.0 ms                                                                                                                 | 62.5 ms: 1.16x slower                                                                                                       |
| genshi_text     | 25.2 ms                                                                                                                 | 29.2 ms: 1.16x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                   | 1.07x slower                                                                                                                |

All benchmarks:
===============

| Benchmark                | results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json | results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| richards                 | 54.4 ms                                                                                                                 | 50.9 ms: 1.07x faster                                                                                                       |
| regex_effbot             | 3.70 ms                                                                                                                 | 3.47 ms: 1.07x faster                                                                                                       |
| richards_super           | 60.4 ms                                                                                                                 | 57.2 ms: 1.06x faster                                                                                                       |
| scimark_sparse_mat_mult  | 4.32 ms                                                                                                                 | 4.14 ms: 1.04x faster                                                                                                       |
| tomli_loads              | 2.21 sec                                                                                                                | 2.14 sec: 1.03x faster                                                                                                      |
| html5lib                 | 75.5 ms                                                                                                                 | 73.4 ms: 1.03x faster                                                                                                       |
| float                    | 78.2 ms                                                                                                                 | 76.2 ms: 1.03x faster                                                                                                       |
| xml_etree_parse          | 150 ms                                                                                                                  | 147 ms: 1.02x faster                                                                                                        |
| mako                     | 10.2 ms                                                                                                                 | 10.0 ms: 1.02x faster                                                                                                       |
| create_gc_cycles         | 1.52 ms                                                                                                                 | 1.50 ms: 1.01x faster                                                                                                       |
| django_template          | 40.9 ms                                                                                                                 | 40.4 ms: 1.01x faster                                                                                                       |
| pickle_dict              | 30.9 us                                                                                                                 | 30.6 us: 1.01x faster                                                                                                       |
| chameleon                | 7.36 ms                                                                                                                 | 7.29 ms: 1.01x faster                                                                                                       |
| xml_etree_iterparse      | 105 ms                                                                                                                  | 104 ms: 1.01x faster                                                                                                        |
| generators               | 33.5 ms                                                                                                                 | 33.3 ms: 1.01x faster                                                                                                       |
| sqlite_synth             | 2.74 us                                                                                                                 | 2.72 us: 1.01x faster                                                                                                       |
| go                       | 173 ms                                                                                                                  | 172 ms: 1.01x faster                                                                                                        |
| pyflate                  | 525 ms                                                                                                                  | 523 ms: 1.00x faster                                                                                                        |
| gc_traversal             | 4.30 ms                                                                                                                 | 4.30 ms: 1.00x faster                                                                                                       |
| pickle                   | 10.2 us                                                                                                                 | 10.2 us: 1.00x slower                                                                                                       |
| pickle_pure_python       | 307 us                                                                                                                  | 308 us: 1.00x slower                                                                                                        |
| asyncio_tcp_ssl          | 1.58 sec                                                                                                                | 1.58 sec: 1.01x slower                                                                                                      |
| regex_v8                 | 25.6 ms                                                                                                                 | 25.7 ms: 1.01x slower                                                                                                       |
| logging_silent           | 96.2 ns                                                                                                                 | 96.9 ns: 1.01x slower                                                                                                       |
| regex_compile            | 144 ms                                                                                                                  | 145 ms: 1.01x slower                                                                                                        |
| json_dumps               | 10.5 ms                                                                                                                 | 10.6 ms: 1.01x slower                                                                                                       |
| json_loads               | 25.2 us                                                                                                                 | 25.4 us: 1.01x slower                                                                                                       |
| logging_simple           | 6.58 us                                                                                                                 | 6.64 us: 1.01x slower                                                                                                       |
| async_tree_io            | 851 ms                                                                                                                  | 860 ms: 1.01x slower                                                                                                        |
| pycparser                | 1.26 sec                                                                                                                | 1.27 sec: 1.01x slower                                                                                                      |
| thrift                   | 868 us                                                                                                                  | 878 us: 1.01x slower                                                                                                        |
| xml_etree_generate       | 82.0 ms                                                                                                                 | 82.9 ms: 1.01x slower                                                                                                       |
| meteor_contest           | 129 ms                                                                                                                  | 130 ms: 1.01x slower                                                                                                        |
| xml_etree_process        | 57.8 ms                                                                                                                 | 58.6 ms: 1.01x slower                                                                                                       |
| asyncio_websockets       | 385 ms                                                                                                                  | 391 ms: 1.02x slower                                                                                                        |
| deepcopy_reduce          | 3.30 us                                                                                                                 | 3.36 us: 1.02x slower                                                                                                       |
| asyncio_tcp              | 371 ms                                                                                                                  | 378 ms: 1.02x slower                                                                                                        |
| dask                     | 392 ms                                                                                                                  | 399 ms: 1.02x slower                                                                                                        |
| tornado_http             | 121 ms                                                                                                                  | 123 ms: 1.02x slower                                                                                                        |
| sqlglot_parse            | 1.38 ms                                                                                                                 | 1.41 ms: 1.02x slower                                                                                                       |
| pickle_list              | 4.37 us                                                                                                                 | 4.49 us: 1.03x slower                                                                                                       |
| unpickle_pure_python     | 223 us                                                                                                                  | 230 us: 1.03x slower                                                                                                        |
| telco                    | 7.91 ms                                                                                                                 | 8.14 ms: 1.03x slower                                                                                                       |
| spectral_norm            | 92.2 ms                                                                                                                 | 94.9 ms: 1.03x slower                                                                                                       |
| docutils                 | 2.96 sec                                                                                                                | 3.04 sec: 1.03x slower                                                                                                      |
| unpickle_list            | 4.47 us                                                                                                                 | 4.60 us: 1.03x slower                                                                                                       |
| sqlglot_transpile        | 1.76 ms                                                                                                                 | 1.82 ms: 1.03x slower                                                                                                       |
| sympy_expand             | 496 ms                                                                                                                  | 512 ms: 1.03x slower                                                                                                        |
| deepcopy                 | 368 us                                                                                                                  | 380 us: 1.03x slower                                                                                                        |
| fannkuch                 | 385 ms                                                                                                                  | 398 ms: 1.03x slower                                                                                                        |
| unpickle                 | 14.6 us                                                                                                                 | 15.1 us: 1.04x slower                                                                                                       |
| mdp                      | 2.49 sec                                                                                                                | 2.58 sec: 1.04x slower                                                                                                      |
| bench_thread_pool        | 902 us                                                                                                                  | 936 us: 1.04x slower                                                                                                        |
| 2to3                     | 291 ms                                                                                                                  | 302 ms: 1.04x slower                                                                                                        |
| aiohttp                  | 1.07 ms                                                                                                                 | 1.11 ms: 1.04x slower                                                                                                       |
| sympy_str                | 290 ms                                                                                                                  | 302 ms: 1.04x slower                                                                                                        |
| sqlglot_normalize        | 118 ms                                                                                                                  | 123 ms: 1.04x slower                                                                                                        |
| deepcopy_memo            | 36.3 us                                                                                                                 | 38.0 us: 1.05x slower                                                                                                       |
| deltablue                | 3.52 ms                                                                                                                 | 3.70 ms: 1.05x slower                                                                                                       |
| coverage                 | 79.9 ms                                                                                                                 | 84.1 ms: 1.05x slower                                                                                                       |
| gunicorn                 | 1.04 ms                                                                                                                 | 1.09 ms: 1.05x slower                                                                                                       |
| sympy_sum                | 152 ms                                                                                                                  | 161 ms: 1.06x slower                                                                                                        |
| pprint_safe_repr         | 789 ms                                                                                                                  | 837 ms: 1.06x slower                                                                                                        |
| pprint_pformat           | 1.61 sec                                                                                                                | 1.71 sec: 1.06x slower                                                                                                      |
| mypy2                    | 771 ms                                                                                                                  | 818 ms: 1.06x slower                                                                                                        |
| sqlglot_optimize         | 59.2 ms                                                                                                                 | 63.0 ms: 1.06x slower                                                                                                       |
| regex_dna                | 233 ms                                                                                                                  | 249 ms: 1.07x slower                                                                                                        |
| scimark_fft              | 296 ms                                                                                                                  | 318 ms: 1.07x slower                                                                                                        |
| typing_runtime_protocols | 113 us                                                                                                                  | 121 us: 1.08x slower                                                                                                        |
| async_generators         | 354 ms                                                                                                                  | 383 ms: 1.08x slower                                                                                                        |
| scimark_sor              | 140 ms                                                                                                                  | 152 ms: 1.09x slower                                                                                                        |
| sympy_integrate          | 23.1 ms                                                                                                                 | 25.1 ms: 1.09x slower                                                                                                       |
| crypto_pyaes             | 71.2 ms                                                                                                                 | 78.6 ms: 1.10x slower                                                                                                       |
| chaos                    | 60.9 ms                                                                                                                 | 67.6 ms: 1.11x slower                                                                                                       |
| python_startup           | 12.7 ms                                                                                                                 | 14.2 ms: 1.12x slower                                                                                                       |
| python_startup_no_site   | 11.0 ms                                                                                                                 | 12.5 ms: 1.14x slower                                                                                                       |
| scimark_monte_carlo      | 66.0 ms                                                                                                                 | 75.9 ms: 1.15x slower                                                                                                       |
| nbody                    | 86.8 ms                                                                                                                 | 100 ms: 1.15x slower                                                                                                        |
| hexiom                   | 6.35 ms                                                                                                                 | 7.34 ms: 1.15x slower                                                                                                       |
| genshi_xml               | 54.0 ms                                                                                                                 | 62.5 ms: 1.16x slower                                                                                                       |
| genshi_text              | 25.2 ms                                                                                                                 | 29.2 ms: 1.16x slower                                                                                                       |
| nqueens                  | 87.5 ms                                                                                                                 | 102 ms: 1.16x slower                                                                                                        |
| raytrace                 | 265 ms                                                                                                                  | 311 ms: 1.17x slower                                                                                                        |
| comprehensions           | 16.7 us                                                                                                                 | 19.6 us: 1.18x slower                                                                                                       |
| scimark_lu               | 94.4 ms                                                                                                                 | 116 ms: 1.23x slower                                                                                                        |
| unpack_sequence          | 48.2 ns                                                                                                                 | 73.6 ns: 1.53x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                   | 1.04x slower                                                                                                                |

Benchmark hidden because not significant (15): coroutines, json, dulwich_log, logging_format, pidigits, pathlib, async_tree_cpu_io_mixed_tg, bench_mp_pool, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, pylint


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.14x