# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: windows-amd64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 210 ms                                                                                                    | 218 ms: 1.04x slower                                                                                                  |
| tornado_http   | 86.1 ms                                                                                                   | 89.4 ms: 1.04x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (2): chameleon, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization | 341 ms                                                                                                    | 346 ms: 1.02x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                     | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                                                    | 148 ms: 1.01x slower                                                                                                  |
| float          | 52.3 ms                                                                                                   | 57.1 ms: 1.09x slower                                                                                                 |
| nbody          | 72.0 ms                                                                                                   | 81.4 ms: 1.13x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.07x slower                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                                                                   | 1.58 ms: 1.03x faster                                                                                                 |
| regex_dna      | 122 ms                                                                                                    | 120 ms: 1.02x faster                                                                                                  |
| regex_compile  | 78.9 ms                                                                                                   | 88.1 ms: 1.12x slower                                                                                                 |
| regex_v8       | 15.3 ms                                                                                                   | 17.9 ms: 1.17x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                     | 1.05x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 2.70 us                                                                                                   | 2.62 us: 1.03x faster                                                                                                 |
| pickle_pure_python   | 179 us                                                                                                    | 175 us: 1.02x faster                                                                                                  |
| json_dumps           | 5.50 ms                                                                                                   | 5.46 ms: 1.01x faster                                                                                                 |
| pickle               | 6.94 us                                                                                                   | 6.96 us: 1.00x slower                                                                                                 |
| json_loads           | 13.4 us                                                                                                   | 13.4 us: 1.00x slower                                                                                                 |
| xml_etree_parse      | 92.3 ms                                                                                                   | 93.0 ms: 1.01x slower                                                                                                 |
| xml_etree_process    | 36.4 ms                                                                                                   | 37.6 ms: 1.03x slower                                                                                                 |
| xml_etree_generate   | 53.2 ms                                                                                                   | 55.1 ms: 1.04x slower                                                                                                 |
| tomli_loads          | 1.37 sec                                                                                                  | 1.43 sec: 1.04x slower                                                                                                |
| xml_etree_iterparse  | 64.5 ms                                                                                                   | 67.5 ms: 1.05x slower                                                                                                 |
| unpickle_pure_python | 128 us                                                                                                    | 136 us: 1.07x slower                                                                                                  |
| pickle_list          | 2.83 us                                                                                                   | 3.32 us: 1.17x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                     | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (2): pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 19.9 ms                                                                                                   | 20.7 ms: 1.04x slower                                                                                                 |
| python_startup_no_site | 17.6 ms                                                                                                   | 19.6 ms: 1.11x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                     | 1.08x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako      | 6.48 ms                                                                                                   | 7.38 ms: 1.14x slower                                                                                                 |

All benchmarks:
===============

| Benchmark                | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 2.02 sec                                                                                                  | 1.66 sec: 1.21x faster                                                                                                |
| scimark_sor              | 85.4 ms                                                                                                   | 78.6 ms: 1.09x faster                                                                                                 |
| pycparser                | 723 ms                                                                                                    | 675 ms: 1.07x faster                                                                                                  |
| unpickle_list            | 2.70 us                                                                                                   | 2.62 us: 1.03x faster                                                                                                 |
| deepcopy_memo            | 23.5 us                                                                                                   | 22.9 us: 1.03x faster                                                                                                 |
| regex_effbot             | 1.62 ms                                                                                                   | 1.58 ms: 1.03x faster                                                                                                 |
| regex_dna                | 122 ms                                                                                                    | 120 ms: 1.02x faster                                                                                                  |
| richards_super           | 30.8 ms                                                                                                   | 30.1 ms: 1.02x faster                                                                                                 |
| pickle_pure_python       | 179 us                                                                                                    | 175 us: 1.02x faster                                                                                                  |
| create_gc_cycles         | 746 us                                                                                                    | 732 us: 1.02x faster                                                                                                  |
| gc_traversal             | 1.52 ms                                                                                                   | 1.49 ms: 1.02x faster                                                                                                 |
| pathlib                  | 79.9 ms                                                                                                   | 78.5 ms: 1.02x faster                                                                                                 |
| coverage                 | 45.8 ms                                                                                                   | 45.2 ms: 1.01x faster                                                                                                 |
| richards                 | 27.3 ms                                                                                                   | 27.0 ms: 1.01x faster                                                                                                 |
| deepcopy                 | 218 us                                                                                                    | 216 us: 1.01x faster                                                                                                  |
| json_dumps               | 5.50 ms                                                                                                   | 5.46 ms: 1.01x faster                                                                                                 |
| pickle                   | 6.94 us                                                                                                   | 6.96 us: 1.00x slower                                                                                                 |
| json_loads               | 13.4 us                                                                                                   | 13.4 us: 1.00x slower                                                                                                 |
| coroutines               | 13.2 ms                                                                                                   | 13.3 ms: 1.00x slower                                                                                                 |
| async_generators         | 227 ms                                                                                                    | 228 ms: 1.01x slower                                                                                                  |
| pidigits                 | 147 ms                                                                                                    | 148 ms: 1.01x slower                                                                                                  |
| sqlite_synth             | 1.56 us                                                                                                   | 1.57 us: 1.01x slower                                                                                                 |
| xml_etree_parse          | 92.3 ms                                                                                                   | 93.0 ms: 1.01x slower                                                                                                 |
| bench_mp_pool            | 64.0 ms                                                                                                   | 64.9 ms: 1.01x slower                                                                                                 |
| generators               | 20.0 ms                                                                                                   | 20.3 ms: 1.01x slower                                                                                                 |
| telco                    | 4.57 ms                                                                                                   | 4.64 ms: 1.02x slower                                                                                                 |
| async_tree_memoization   | 341 ms                                                                                                    | 346 ms: 1.02x slower                                                                                                  |
| scimark_lu               | 56.4 ms                                                                                                   | 57.6 ms: 1.02x slower                                                                                                 |
| asyncio_tcp              | 465 ms                                                                                                    | 477 ms: 1.02x slower                                                                                                  |
| logging_silent           | 54.1 ns                                                                                                   | 55.5 ns: 1.02x slower                                                                                                 |
| logging_simple           | 6.07 us                                                                                                   | 6.24 us: 1.03x slower                                                                                                 |
| xml_etree_process        | 36.4 ms                                                                                                   | 37.6 ms: 1.03x slower                                                                                                 |
| dulwich_log              | 41.4 ms                                                                                                   | 42.8 ms: 1.04x slower                                                                                                 |
| xml_etree_generate       | 53.2 ms                                                                                                   | 55.1 ms: 1.04x slower                                                                                                 |
| sqlglot_parse            | 752 us                                                                                                    | 779 us: 1.04x slower                                                                                                  |
| 2to3                     | 210 ms                                                                                                    | 218 ms: 1.04x slower                                                                                                  |
| logging_format           | 6.51 us                                                                                                   | 6.76 us: 1.04x slower                                                                                                 |
| tornado_http             | 86.1 ms                                                                                                   | 89.4 ms: 1.04x slower                                                                                                 |
| typing_runtime_protocols | 73.9 us                                                                                                   | 77.0 us: 1.04x slower                                                                                                 |
| python_startup           | 19.9 ms                                                                                                   | 20.7 ms: 1.04x slower                                                                                                 |
| tomli_loads              | 1.37 sec                                                                                                  | 1.43 sec: 1.04x slower                                                                                                |
| sqlglot_transpile        | 965 us                                                                                                    | 1.01 ms: 1.04x slower                                                                                                 |
| sympy_expand             | 269 ms                                                                                                    | 281 ms: 1.04x slower                                                                                                  |
| xml_etree_iterparse      | 64.5 ms                                                                                                   | 67.5 ms: 1.05x slower                                                                                                 |
| mdp                      | 1.36 sec                                                                                                  | 1.44 sec: 1.06x slower                                                                                                |
| unpickle_pure_python     | 128 us                                                                                                    | 136 us: 1.07x slower                                                                                                  |
| meteor_contest           | 72.6 ms                                                                                                   | 77.5 ms: 1.07x slower                                                                                                 |
| sqlglot_normalize        | 171 ms                                                                                                    | 183 ms: 1.07x slower                                                                                                  |
| sqlglot_optimize         | 32.5 ms                                                                                                   | 34.8 ms: 1.07x slower                                                                                                 |
| sympy_str                | 156 ms                                                                                                    | 168 ms: 1.08x slower                                                                                                  |
| sympy_sum                | 82.3 ms                                                                                                   | 89.1 ms: 1.08x slower                                                                                                 |
| pprint_safe_repr         | 479 ms                                                                                                    | 519 ms: 1.08x slower                                                                                                  |
| sympy_integrate          | 12.2 ms                                                                                                   | 13.3 ms: 1.09x slower                                                                                                 |
| raytrace                 | 163 ms                                                                                                    | 177 ms: 1.09x slower                                                                                                  |
| float                    | 52.3 ms                                                                                                   | 57.1 ms: 1.09x slower                                                                                                 |
| json                     | 2.85 ms                                                                                                   | 3.11 ms: 1.09x slower                                                                                                 |
| go                       | 84.3 ms                                                                                                   | 92.1 ms: 1.09x slower                                                                                                 |
| pprint_pformat           | 979 ms                                                                                                    | 1.07 sec: 1.10x slower                                                                                                |
| python_startup_no_site   | 17.6 ms                                                                                                   | 19.6 ms: 1.11x slower                                                                                                 |
| pyflate                  | 291 ms                                                                                                    | 324 ms: 1.11x slower                                                                                                  |
| regex_compile            | 78.9 ms                                                                                                   | 88.1 ms: 1.12x slower                                                                                                 |
| nqueens                  | 58.2 ms                                                                                                   | 65.3 ms: 1.12x slower                                                                                                 |
| nbody                    | 72.0 ms                                                                                                   | 81.4 ms: 1.13x slower                                                                                                 |
| chaos                    | 39.2 ms                                                                                                   | 44.4 ms: 1.13x slower                                                                                                 |
| crypto_pyaes             | 43.3 ms                                                                                                   | 49.2 ms: 1.14x slower                                                                                                 |
| mako                     | 6.48 ms                                                                                                   | 7.38 ms: 1.14x slower                                                                                                 |
| fannkuch                 | 241 ms                                                                                                    | 277 ms: 1.15x slower                                                                                                  |
| scimark_fft              | 184 ms                                                                                                    | 213 ms: 1.16x slower                                                                                                  |
| regex_v8                 | 15.3 ms                                                                                                   | 17.9 ms: 1.17x slower                                                                                                 |
| pickle_list              | 2.83 us                                                                                                   | 3.32 us: 1.17x slower                                                                                                 |
| scimark_monte_carlo      | 40.9 ms                                                                                                   | 49.4 ms: 1.21x slower                                                                                                 |
| comprehensions           | 10.3 us                                                                                                   | 12.9 us: 1.25x slower                                                                                                 |
| scimark_sparse_mat_mult  | 2.46 ms                                                                                                   | 3.09 ms: 1.26x slower                                                                                                 |
| hexiom                   | 3.81 ms                                                                                                   | 5.03 ms: 1.32x slower                                                                                                 |
| spectral_norm            | 63.6 ms                                                                                                   | 84.1 ms: 1.32x slower                                                                                                 |
| deltablue                | 2.01 ms                                                                                                   | 2.72 ms: 1.35x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                     | 1.05x slower                                                                                                          |

Benchmark hidden because not significant (14): pickle_dict, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, deepcopy_reduce, docutils, unpickle, async_tree_none_tg, async_tree_cpu_io_mixed, chameleon, async_tree_memoization_tg, mypy2, bench_thread_pool, async_tree_none
Ignored benchmarks (8) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown