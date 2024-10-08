# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.00x slower
- HPT reliability: 83.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                                                                    | 217 ms: 1.01x slower                                                                                          |
| chameleon      | 5.01 ms                                                                                                   | 4.74 ms: 1.06x faster                                                                                         |
| docutils       | 1.55 sec                                                                                                  | 1.56 sec: 1.01x slower                                                                                        |
| tornado_http   | 84.3 ms                                                                                                   | 85.5 ms: 1.01x slower                                                                                         |
| Geometric mean | (ref)                                                                                                     | 1.01x faster                                                                                                  |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| nbody          | 73.2 ms                                                                                                   | 61.0 ms: 1.20x faster                                                                                         |
| pidigits       | 148 ms                                                                                                    | 151 ms: 1.02x slower                                                                                          |
| Geometric mean | (ref)                                                                                                     | 1.05x faster                                                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.4 ms                                                                                                   | 14.3 ms: 1.01x faster                                                                                         |
| regex_compile  | 77.8 ms                                                                                                   | 79.3 ms: 1.02x slower                                                                                         |
| regex_dna      | 115 ms                                                                                                    | 118 ms: 1.03x slower                                                                                          |
| Geometric mean | (ref)                                                                                                     | 1.01x slower                                                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.43 sec                                                                                                  | 1.30 sec: 1.10x faster                                                                                        |
| pickle_pure_python   | 186 us                                                                                                    | 174 us: 1.07x faster                                                                                          |
| pickle_list          | 2.96 us                                                                                                   | 2.78 us: 1.07x faster                                                                                         |
| xml_etree_generate   | 54.5 ms                                                                                                   | 51.9 ms: 1.05x faster                                                                                         |
| pickle_dict          | 18.4 us                                                                                                   | 17.6 us: 1.04x faster                                                                                         |
| xml_etree_iterparse  | 65.1 ms                                                                                                   | 62.9 ms: 1.04x faster                                                                                         |
| xml_etree_process    | 37.1 ms                                                                                                   | 35.9 ms: 1.03x faster                                                                                         |
| unpickle             | 8.66 us                                                                                                   | 8.41 us: 1.03x faster                                                                                         |
| unpickle_pure_python | 129 us                                                                                                    | 126 us: 1.02x faster                                                                                          |
| xml_etree_parse      | 92.2 ms                                                                                                   | 91.2 ms: 1.01x faster                                                                                         |
| json_dumps           | 5.58 ms                                                                                                   | 5.54 ms: 1.01x faster                                                                                         |
| json_loads           | 13.7 us                                                                                                   | 13.8 us: 1.01x slower                                                                                         |
| unpickle_list        | 2.68 us                                                                                                   | 2.74 us: 1.02x slower                                                                                         |
| Geometric mean       | (ref)                                                                                                     | 1.03x faster                                                                                                  |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.2 ms                                                                                                   | 20.5 ms: 1.02x slower                                                                                         |
| python_startup_no_site | 17.8 ms                                                                                                   | 18.5 ms: 1.04x slower                                                                                         |
| Geometric mean         | (ref)                                                                                                     | 1.03x slower                                                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| mako      | 6.29 ms                                                                                                   | 6.71 ms: 1.07x slower                                                                                         |

All benchmarks:
===============

| Benchmark                | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|
| nbody                    | 73.2 ms                                                                                                   | 61.0 ms: 1.20x faster                                                                                         |
| richards                 | 28.0 ms                                                                                                   | 24.8 ms: 1.13x faster                                                                                         |
| richards_super           | 31.6 ms                                                                                                   | 28.2 ms: 1.12x faster                                                                                         |
| tomli_loads              | 1.43 sec                                                                                                  | 1.30 sec: 1.10x faster                                                                                        |
| deepcopy_memo            | 23.0 us                                                                                                   | 21.3 us: 1.08x faster                                                                                         |
| deepcopy                 | 233 us                                                                                                    | 217 us: 1.07x faster                                                                                          |
| pathlib                  | 80.8 ms                                                                                                   | 75.3 ms: 1.07x faster                                                                                         |
| pickle_pure_python       | 186 us                                                                                                    | 174 us: 1.07x faster                                                                                          |
| deepcopy_reduce          | 2.05 us                                                                                                   | 1.92 us: 1.07x faster                                                                                         |
| pickle_list              | 2.96 us                                                                                                   | 2.78 us: 1.07x faster                                                                                         |
| logging_silent           | 57.3 ns                                                                                                   | 54.0 ns: 1.06x faster                                                                                         |
| chameleon                | 5.01 ms                                                                                                   | 4.74 ms: 1.06x faster                                                                                         |
| xml_etree_generate       | 54.5 ms                                                                                                   | 51.9 ms: 1.05x faster                                                                                         |
| generators               | 20.8 ms                                                                                                   | 19.9 ms: 1.05x faster                                                                                         |
| pickle_dict              | 18.4 us                                                                                                   | 17.6 us: 1.04x faster                                                                                         |
| pprint_pformat           | 1.02 sec                                                                                                  | 980 ms: 1.04x faster                                                                                          |
| pprint_safe_repr         | 500 ms                                                                                                    | 480 ms: 1.04x faster                                                                                          |
| xml_etree_iterparse      | 65.1 ms                                                                                                   | 62.9 ms: 1.04x faster                                                                                         |
| xml_etree_process        | 37.1 ms                                                                                                   | 35.9 ms: 1.03x faster                                                                                         |
| telco                    | 4.73 ms                                                                                                   | 4.57 ms: 1.03x faster                                                                                         |
| logging_simple           | 6.15 us                                                                                                   | 5.95 us: 1.03x faster                                                                                         |
| fannkuch                 | 250 ms                                                                                                    | 242 ms: 1.03x faster                                                                                          |
| unpickle                 | 8.66 us                                                                                                   | 8.41 us: 1.03x faster                                                                                         |
| logging_format           | 6.57 us                                                                                                   | 6.39 us: 1.03x faster                                                                                         |
| scimark_sor              | 77.9 ms                                                                                                   | 76.0 ms: 1.02x faster                                                                                         |
| dulwich_log              | 41.3 ms                                                                                                   | 40.4 ms: 1.02x faster                                                                                         |
| unpickle_pure_python     | 129 us                                                                                                    | 126 us: 1.02x faster                                                                                          |
| typing_runtime_protocols | 71.0 us                                                                                                   | 69.7 us: 1.02x faster                                                                                         |
| sqlglot_parse            | 768 us                                                                                                    | 755 us: 1.02x faster                                                                                          |
| sqlglot_normalize        | 176 ms                                                                                                    | 173 ms: 1.02x faster                                                                                          |
| comprehensions           | 10.8 us                                                                                                   | 10.6 us: 1.01x faster                                                                                         |
| sqlite_synth             | 1.53 us                                                                                                   | 1.51 us: 1.01x faster                                                                                         |
| xml_etree_parse          | 92.2 ms                                                                                                   | 91.2 ms: 1.01x faster                                                                                         |
| regex_v8                 | 14.4 ms                                                                                                   | 14.3 ms: 1.01x faster                                                                                         |
| json_dumps               | 5.58 ms                                                                                                   | 5.54 ms: 1.01x faster                                                                                         |
| sqlglot_transpile        | 983 us                                                                                                    | 978 us: 1.01x faster                                                                                          |
| sqlglot_optimize         | 33.4 ms                                                                                                   | 33.5 ms: 1.00x slower                                                                                         |
| scimark_lu               | 55.0 ms                                                                                                   | 55.3 ms: 1.00x slower                                                                                         |
| raytrace                 | 165 ms                                                                                                    | 166 ms: 1.01x slower                                                                                          |
| docutils                 | 1.55 sec                                                                                                  | 1.56 sec: 1.01x slower                                                                                        |
| json_loads               | 13.7 us                                                                                                   | 13.8 us: 1.01x slower                                                                                         |
| tornado_http             | 84.3 ms                                                                                                   | 85.5 ms: 1.01x slower                                                                                         |
| sympy_expand             | 274 ms                                                                                                    | 277 ms: 1.01x slower                                                                                          |
| 2to3                     | 214 ms                                                                                                    | 217 ms: 1.01x slower                                                                                          |
| python_startup           | 20.2 ms                                                                                                   | 20.5 ms: 1.02x slower                                                                                         |
| mypy2                    | 416 ms                                                                                                    | 423 ms: 1.02x slower                                                                                          |
| regex_compile            | 77.8 ms                                                                                                   | 79.3 ms: 1.02x slower                                                                                         |
| sympy_str                | 160 ms                                                                                                    | 163 ms: 1.02x slower                                                                                          |
| unpickle_list            | 2.68 us                                                                                                   | 2.74 us: 1.02x slower                                                                                         |
| coverage                 | 47.3 ms                                                                                                   | 48.4 ms: 1.02x slower                                                                                         |
| pidigits                 | 148 ms                                                                                                    | 151 ms: 1.02x slower                                                                                          |
| nqueens                  | 58.2 ms                                                                                                   | 59.7 ms: 1.03x slower                                                                                         |
| regex_dna                | 115 ms                                                                                                    | 118 ms: 1.03x slower                                                                                          |
| async_generators         | 230 ms                                                                                                    | 238 ms: 1.04x slower                                                                                          |
| sympy_integrate          | 12.4 ms                                                                                                   | 12.8 ms: 1.04x slower                                                                                         |
| sympy_sum                | 83.5 ms                                                                                                   | 86.8 ms: 1.04x slower                                                                                         |
| python_startup_no_site   | 17.8 ms                                                                                                   | 18.5 ms: 1.04x slower                                                                                         |
| scimark_fft              | 179 ms                                                                                                    | 189 ms: 1.05x slower                                                                                          |
| chaos                    | 39.5 ms                                                                                                   | 41.7 ms: 1.06x slower                                                                                         |
| meteor_contest           | 72.2 ms                                                                                                   | 76.7 ms: 1.06x slower                                                                                         |
| scimark_sparse_mat_mult  | 2.49 ms                                                                                                   | 2.65 ms: 1.06x slower                                                                                         |
| mako                     | 6.29 ms                                                                                                   | 6.71 ms: 1.07x slower                                                                                         |
| crypto_pyaes             | 42.8 ms                                                                                                   | 45.8 ms: 1.07x slower                                                                                         |
| spectral_norm            | 59.0 ms                                                                                                   | 63.3 ms: 1.07x slower                                                                                         |
| pyflate                  | 285 ms                                                                                                    | 308 ms: 1.08x slower                                                                                          |
| mdp                      | 1.34 sec                                                                                                  | 1.49 sec: 1.11x slower                                                                                        |
| go                       | 84.4 ms                                                                                                   | 94.8 ms: 1.12x slower                                                                                         |
| hexiom                   | 3.82 ms                                                                                                   | 5.14 ms: 1.35x slower                                                                                         |
| scimark_monte_carlo      | 40.7 ms                                                                                                   | 56.9 ms: 1.40x slower                                                                                         |
| Geometric mean           | (ref)                                                                                                     | 1.00x slower                                                                                                  |

Benchmark hidden because not significant (21): asyncio_tcp_ssl, create_gc_cycles, pycparser, bench_thread_pool, async_tree_io, asyncio_tcp, async_tree_none_tg, coroutines, regex_effbot, pickle, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, deltablue, async_tree_none, bench_mp_pool, async_tree_cpu_io_mixed, gc_traversal, float, json
Ignored benchmarks (8) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 83.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown