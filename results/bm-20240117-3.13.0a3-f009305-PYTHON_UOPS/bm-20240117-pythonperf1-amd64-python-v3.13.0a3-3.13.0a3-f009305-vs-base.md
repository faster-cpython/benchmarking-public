# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 210 ms                                                                                                    | 217 ms: 1.03x slower                                                                                                  |
| chameleon      | 4.91 ms                                                                                                   | 5.10 ms: 1.04x slower                                                                                                 |
| docutils       | 1.53 sec                                                                                                  | 1.59 sec: 1.04x slower                                                                                                |
| tornado_http   | 85.5 ms                                                                                                   | 88.2 ms: 1.03x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.03x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|--------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg | 270 ms                                                                                                    | 275 ms: 1.02x slower                                                                                                  |
| Geometric mean     | (ref)                                                                                                     | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 52.5 ms                                                                                                   | 55.5 ms: 1.06x slower                                                                                                 |
| nbody          | 74.1 ms                                                                                                   | 79.2 ms: 1.07x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 121 ms                                                                                                    | 122 ms: 1.01x slower                                                                                                  |
| regex_effbot   | 1.59 ms                                                                                                   | 1.60 ms: 1.01x slower                                                                                                 |
| regex_v8       | 15.3 ms                                                                                                   | 15.5 ms: 1.02x slower                                                                                                 |
| regex_compile  | 77.7 ms                                                                                                   | 84.2 ms: 1.08x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.03x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle             | 8.42 us                                                                                                   | 8.21 us: 1.03x faster                                                                                                 |
| tomli_loads          | 1.39 sec                                                                                                  | 1.38 sec: 1.01x faster                                                                                                |
| json_loads           | 13.7 us                                                                                                   | 13.6 us: 1.01x faster                                                                                                 |
| pickle               | 7.31 us                                                                                                   | 7.37 us: 1.01x slower                                                                                                 |
| json_dumps           | 5.54 ms                                                                                                   | 5.59 ms: 1.01x slower                                                                                                 |
| xml_etree_parse      | 93.0 ms                                                                                                   | 94.0 ms: 1.01x slower                                                                                                 |
| pickle_pure_python   | 179 us                                                                                                    | 182 us: 1.02x slower                                                                                                  |
| xml_etree_process    | 36.4 ms                                                                                                   | 37.3 ms: 1.03x slower                                                                                                 |
| xml_etree_generate   | 53.6 ms                                                                                                   | 55.2 ms: 1.03x slower                                                                                                 |
| pickle_dict          | 18.2 us                                                                                                   | 18.8 us: 1.03x slower                                                                                                 |
| xml_etree_iterparse  | 63.5 ms                                                                                                   | 67.5 ms: 1.06x slower                                                                                                 |
| pickle_list          | 2.89 us                                                                                                   | 3.08 us: 1.06x slower                                                                                                 |
| unpickle_pure_python | 128 us                                                                                                    | 137 us: 1.07x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                     | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.1 ms                                                                                                   | 20.7 ms: 1.03x slower                                                                                                 |
| python_startup_no_site | 17.9 ms                                                                                                   | 18.5 ms: 1.03x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                     | 1.03x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako      | 6.57 ms                                                                                                   | 7.29 ms: 1.11x slower                                                                                                 |

All benchmarks:
===============

| Benchmark                | results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 1.83 sec                                                                                                  | 1.62 sec: 1.13x faster                                                                                                |
| generators               | 22.1 ms                                                                                                   | 20.6 ms: 1.08x faster                                                                                                 |
| unpickle                 | 8.42 us                                                                                                   | 8.21 us: 1.03x faster                                                                                                 |
| telco                    | 4.77 ms                                                                                                   | 4.66 ms: 1.02x faster                                                                                                 |
| gc_traversal             | 1.52 ms                                                                                                   | 1.49 ms: 1.02x faster                                                                                                 |
| richards                 | 27.4 ms                                                                                                   | 27.0 ms: 1.01x faster                                                                                                 |
| pathlib                  | 79.3 ms                                                                                                   | 78.3 ms: 1.01x faster                                                                                                 |
| richards_super           | 30.8 ms                                                                                                   | 30.5 ms: 1.01x faster                                                                                                 |
| tomli_loads              | 1.39 sec                                                                                                  | 1.38 sec: 1.01x faster                                                                                                |
| json_loads               | 13.7 us                                                                                                   | 13.6 us: 1.01x faster                                                                                                 |
| sqlite_synth             | 1.57 us                                                                                                   | 1.57 us: 1.00x slower                                                                                                 |
| regex_dna                | 121 ms                                                                                                    | 122 ms: 1.01x slower                                                                                                  |
| bench_mp_pool            | 66.6 ms                                                                                                   | 67.1 ms: 1.01x slower                                                                                                 |
| pickle                   | 7.31 us                                                                                                   | 7.37 us: 1.01x slower                                                                                                 |
| regex_effbot             | 1.59 ms                                                                                                   | 1.60 ms: 1.01x slower                                                                                                 |
| json_dumps               | 5.54 ms                                                                                                   | 5.59 ms: 1.01x slower                                                                                                 |
| xml_etree_parse          | 93.0 ms                                                                                                   | 94.0 ms: 1.01x slower                                                                                                 |
| pickle_pure_python       | 179 us                                                                                                    | 182 us: 1.02x slower                                                                                                  |
| async_tree_none_tg       | 270 ms                                                                                                    | 275 ms: 1.02x slower                                                                                                  |
| regex_v8                 | 15.3 ms                                                                                                   | 15.5 ms: 1.02x slower                                                                                                 |
| sqlglot_transpile        | 981 us                                                                                                    | 1000 us: 1.02x slower                                                                                                 |
| logging_silent           | 54.1 ns                                                                                                   | 55.3 ns: 1.02x slower                                                                                                 |
| sqlglot_parse            | 761 us                                                                                                    | 778 us: 1.02x slower                                                                                                  |
| scimark_sor              | 78.0 ms                                                                                                   | 79.9 ms: 1.03x slower                                                                                                 |
| xml_etree_process        | 36.4 ms                                                                                                   | 37.3 ms: 1.03x slower                                                                                                 |
| sqlglot_normalize        | 175 ms                                                                                                    | 180 ms: 1.03x slower                                                                                                  |
| python_startup           | 20.1 ms                                                                                                   | 20.7 ms: 1.03x slower                                                                                                 |
| xml_etree_generate       | 53.6 ms                                                                                                   | 55.2 ms: 1.03x slower                                                                                                 |
| logging_simple           | 6.04 us                                                                                                   | 6.23 us: 1.03x slower                                                                                                 |
| tornado_http             | 85.5 ms                                                                                                   | 88.2 ms: 1.03x slower                                                                                                 |
| python_startup_no_site   | 17.9 ms                                                                                                   | 18.5 ms: 1.03x slower                                                                                                 |
| 2to3                     | 210 ms                                                                                                    | 217 ms: 1.03x slower                                                                                                  |
| pickle_dict              | 18.2 us                                                                                                   | 18.8 us: 1.03x slower                                                                                                 |
| deepcopy                 | 223 us                                                                                                    | 230 us: 1.03x slower                                                                                                  |
| bench_thread_pool        | 839 us                                                                                                    | 867 us: 1.03x slower                                                                                                  |
| docutils                 | 1.53 sec                                                                                                  | 1.59 sec: 1.04x slower                                                                                                |
| logging_format           | 6.47 us                                                                                                   | 6.70 us: 1.04x slower                                                                                                 |
| dulwich_log              | 41.1 ms                                                                                                   | 42.6 ms: 1.04x slower                                                                                                 |
| mypy2                    | 409 ms                                                                                                    | 424 ms: 1.04x slower                                                                                                  |
| scimark_lu               | 54.9 ms                                                                                                   | 56.9 ms: 1.04x slower                                                                                                 |
| coverage                 | 44.3 ms                                                                                                   | 46.0 ms: 1.04x slower                                                                                                 |
| chameleon                | 4.91 ms                                                                                                   | 5.10 ms: 1.04x slower                                                                                                 |
| sympy_expand             | 268 ms                                                                                                    | 279 ms: 1.04x slower                                                                                                  |
| sympy_sum                | 82.6 ms                                                                                                   | 86.6 ms: 1.05x slower                                                                                                 |
| sqlglot_optimize         | 33.0 ms                                                                                                   | 34.6 ms: 1.05x slower                                                                                                 |
| deepcopy_reduce          | 1.93 us                                                                                                   | 2.02 us: 1.05x slower                                                                                                 |
| mdp                      | 1.40 sec                                                                                                  | 1.47 sec: 1.05x slower                                                                                                |
| float                    | 52.5 ms                                                                                                   | 55.5 ms: 1.06x slower                                                                                                 |
| meteor_contest           | 71.9 ms                                                                                                   | 76.2 ms: 1.06x slower                                                                                                 |
| nqueens                  | 59.3 ms                                                                                                   | 63.0 ms: 1.06x slower                                                                                                 |
| xml_etree_iterparse      | 63.5 ms                                                                                                   | 67.5 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols | 70.5 us                                                                                                   | 74.9 us: 1.06x slower                                                                                                 |
| sympy_str                | 156 ms                                                                                                    | 166 ms: 1.06x slower                                                                                                  |
| pickle_list              | 2.89 us                                                                                                   | 3.08 us: 1.06x slower                                                                                                 |
| unpickle_pure_python     | 128 us                                                                                                    | 137 us: 1.07x slower                                                                                                  |
| sympy_integrate          | 12.3 ms                                                                                                   | 13.1 ms: 1.07x slower                                                                                                 |
| go                       | 84.9 ms                                                                                                   | 90.8 ms: 1.07x slower                                                                                                 |
| nbody                    | 74.1 ms                                                                                                   | 79.2 ms: 1.07x slower                                                                                                 |
| deepcopy_memo            | 22.2 us                                                                                                   | 23.7 us: 1.07x slower                                                                                                 |
| pprint_safe_repr         | 491 ms                                                                                                    | 528 ms: 1.08x slower                                                                                                  |
| fannkuch                 | 245 ms                                                                                                    | 264 ms: 1.08x slower                                                                                                  |
| regex_compile            | 77.7 ms                                                                                                   | 84.2 ms: 1.08x slower                                                                                                 |
| raytrace                 | 161 ms                                                                                                    | 174 ms: 1.08x slower                                                                                                  |
| pprint_pformat           | 1.00 sec                                                                                                  | 1.09 sec: 1.09x slower                                                                                                |
| mako                     | 6.57 ms                                                                                                   | 7.29 ms: 1.11x slower                                                                                                 |
| chaos                    | 39.5 ms                                                                                                   | 44.0 ms: 1.11x slower                                                                                                 |
| crypto_pyaes             | 42.8 ms                                                                                                   | 47.7 ms: 1.12x slower                                                                                                 |
| pyflate                  | 288 ms                                                                                                    | 323 ms: 1.12x slower                                                                                                  |
| scimark_fft              | 178 ms                                                                                                    | 203 ms: 1.14x slower                                                                                                  |
| scimark_sparse_mat_mult  | 2.52 ms                                                                                                   | 2.95 ms: 1.17x slower                                                                                                 |
| scimark_monte_carlo      | 39.9 ms                                                                                                   | 47.5 ms: 1.19x slower                                                                                                 |
| json                     | 2.88 ms                                                                                                   | 3.52 ms: 1.22x slower                                                                                                 |
| comprehensions           | 10.3 us                                                                                                   | 12.7 us: 1.24x slower                                                                                                 |
| hexiom                   | 3.82 ms                                                                                                   | 4.82 ms: 1.26x slower                                                                                                 |
| spectral_norm            | 61.6 ms                                                                                                   | 79.9 ms: 1.30x slower                                                                                                 |
| deltablue                | 1.97 ms                                                                                                   | 2.60 ms: 1.32x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                     | 1.04x slower                                                                                                          |

Benchmark hidden because not significant (14): pycparser, coroutines, async_tree_io_tg, async_tree_io, pidigits, unpickle_list, async_generators, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, create_gc_cycles, async_tree_none, asyncio_tcp, async_tree_memoization_tg
Ignored benchmarks (8) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown