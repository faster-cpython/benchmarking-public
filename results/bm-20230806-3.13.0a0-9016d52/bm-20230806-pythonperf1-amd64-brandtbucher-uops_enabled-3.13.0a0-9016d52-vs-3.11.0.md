
# Results vs. 3.11.0

- fork: brandtbucher
- ref: uops_enabled
- machine: windows-amd64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.76 sec: 1.10x slower                                                   |
| Geometric mean | (ref)                                                       | 1.05x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 59.1 ms: 1.08x slower                                                    |
| nbody          | 70.0 ms                                                     | 82.6 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                       | 1.08x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                    |
| regex_dna      | 115 ms                                                      | 122 ms: 1.05x slower                                                     |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                    |
| regex_compile  | 90.6 ms                                                     | 101 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                       | 1.06x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.87 ms: 1.29x faster                                                    |
| xml_etree_parse      | 95.9 ms                                                     | 93.2 ms: 1.03x faster                                                    |
| pickle_pure_python   | 200 us                                                      | 202 us: 1.01x slower                                                     |
| unpickle_pure_python | 152 us                                                      | 154 us: 1.01x slower                                                     |
| unpickle             | 8.09 us                                                     | 8.21 us: 1.02x slower                                                    |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                                    |
| pickle_list          | 2.68 us                                                     | 2.87 us: 1.07x slower                                                    |
| xml_etree_iterparse  | 62.6 ms                                                     | 68.4 ms: 1.09x slower                                                    |
| xml_etree_process    | 37.1 ms                                                     | 41.0 ms: 1.10x slower                                                    |
| pickle               | 6.61 us                                                     | 7.45 us: 1.13x slower                                                    |
| xml_etree_generate   | 52.2 ms                                                     | 59.9 ms: 1.15x slower                                                    |
| unpickle_list        | 2.55 us                                                     | 2.93 us: 1.15x slower                                                    |
| tomli_loads          | 1.41 sec                                                    | 1.77 sec: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                    |
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 8.28 ms: 1.14x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 102 us: 3.16x faster                                                     |
| asyncio_tcp              | 699 ms                                                      | 514 ms: 1.36x faster                                                     |
| generators               | 33.8 ms                                                     | 25.7 ms: 1.31x faster                                                    |
| json_dumps               | 7.56 ms                                                     | 5.87 ms: 1.29x faster                                                    |
| unpack_sequence          | 46.1 ns                                                     | 39.9 ns: 1.15x faster                                                    |
| json                     | 3.25 ms                                                     | 2.92 ms: 1.12x faster                                                    |
| raytrace                 | 211 ms                                                      | 194 ms: 1.08x faster                                                     |
| mdp                      | 1.67 sec                                                    | 1.57 sec: 1.07x faster                                                   |
| coverage                 | 55.9 ms                                                     | 52.9 ms: 1.06x faster                                                    |
| sqlglot_parse            | 952 us                                                      | 903 us: 1.05x faster                                                     |
| richards_super           | 37.5 ms                                                     | 35.8 ms: 1.05x faster                                                    |
| deltablue                | 2.61 ms                                                     | 2.50 ms: 1.04x faster                                                    |
| logging_silent           | 69.8 ns                                                     | 67.5 ns: 1.03x faster                                                    |
| xml_etree_parse          | 95.9 ms                                                     | 93.2 ms: 1.03x faster                                                    |
| async_tree_none          | 320 ms                                                      | 312 ms: 1.03x faster                                                     |
| async_tree_memoization   | 371 ms                                                      | 364 ms: 1.02x faster                                                     |
| sqlglot_transpile        | 1.16 ms                                                     | 1.14 ms: 1.02x faster                                                    |
| regex_v8                 | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                    |
| pickle_pure_python       | 200 us                                                      | 202 us: 1.01x slower                                                     |
| chaos                    | 47.1 ms                                                     | 47.8 ms: 1.01x slower                                                    |
| unpickle_pure_python     | 152 us                                                      | 154 us: 1.01x slower                                                     |
| unpickle                 | 8.09 us                                                     | 8.21 us: 1.02x slower                                                    |
| python_startup           | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                    |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.6 ms: 1.02x slower                                                    |
| python_startup_no_site   | 15.9 ms                                                     | 16.3 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 514 ms: 1.03x slower                                                     |
| crypto_pyaes             | 47.6 ms                                                     | 49.0 ms: 1.03x slower                                                    |
| richards                 | 30.6 ms                                                     | 32.0 ms: 1.05x slower                                                    |
| bench_thread_pool        | 852 us                                                      | 894 us: 1.05x slower                                                     |
| sqlglot_normalize        | 190 ms                                                      | 200 ms: 1.05x slower                                                     |
| regex_dna                | 115 ms                                                      | 122 ms: 1.05x slower                                                     |
| spectral_norm            | 67.9 ms                                                     | 71.7 ms: 1.05x slower                                                    |
| coroutines               | 14.6 ms                                                     | 15.4 ms: 1.06x slower                                                    |
| sqlite_synth             | 1.68 us                                                     | 1.78 us: 1.06x slower                                                    |
| scimark_lu               | 63.5 ms                                                     | 67.3 ms: 1.06x slower                                                    |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                                    |
| gc_traversal             | 1.46 ms                                                     | 1.55 ms: 1.06x slower                                                    |
| deepcopy                 | 246 us                                                      | 262 us: 1.07x slower                                                     |
| pprint_safe_repr         | 512 ms                                                      | 548 ms: 1.07x slower                                                     |
| pickle_list              | 2.68 us                                                     | 2.87 us: 1.07x slower                                                    |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                    |
| create_gc_cycles         | 693 us                                                      | 747 us: 1.08x slower                                                     |
| float                    | 54.6 ms                                                     | 59.1 ms: 1.08x slower                                                    |
| dulwich_log              | 44.5 ms                                                     | 48.2 ms: 1.08x slower                                                    |
| pprint_pformat           | 1.04 sec                                                    | 1.13 sec: 1.08x slower                                                   |
| bench_mp_pool            | 62.5 ms                                                     | 68.0 ms: 1.09x slower                                                    |
| sqlglot_optimize         | 34.9 ms                                                     | 38.0 ms: 1.09x slower                                                    |
| go                       | 97.3 ms                                                     | 106 ms: 1.09x slower                                                     |
| xml_etree_iterparse      | 62.6 ms                                                     | 68.4 ms: 1.09x slower                                                    |
| docutils                 | 1.60 sec                                                    | 1.76 sec: 1.10x slower                                                   |
| deepcopy_reduce          | 2.07 us                                                     | 2.28 us: 1.10x slower                                                    |
| xml_etree_process        | 37.1 ms                                                     | 41.0 ms: 1.10x slower                                                    |
| regex_compile            | 90.6 ms                                                     | 101 ms: 1.11x slower                                                     |
| logging_simple           | 6.61 us                                                     | 7.37 us: 1.11x slower                                                    |
| pycparser                | 691 ms                                                      | 772 ms: 1.12x slower                                                     |
| meteor_contest           | 74.7 ms                                                     | 83.8 ms: 1.12x slower                                                    |
| logging_format           | 7.01 us                                                     | 7.89 us: 1.13x slower                                                    |
| pickle                   | 6.61 us                                                     | 7.45 us: 1.13x slower                                                    |
| mako                     | 7.26 ms                                                     | 8.28 ms: 1.14x slower                                                    |
| comprehensions           | 15.9 us                                                     | 18.2 us: 1.14x slower                                                    |
| deepcopy_memo            | 25.2 us                                                     | 28.7 us: 1.14x slower                                                    |
| pyflate                  | 304 ms                                                      | 348 ms: 1.14x slower                                                     |
| xml_etree_generate       | 52.2 ms                                                     | 59.9 ms: 1.15x slower                                                    |
| unpickle_list            | 2.55 us                                                     | 2.93 us: 1.15x slower                                                    |
| nqueens                  | 64.9 ms                                                     | 74.6 ms: 1.15x slower                                                    |
| scimark_fft              | 178 ms                                                      | 205 ms: 1.15x slower                                                     |
| scimark_sor              | 75.6 ms                                                     | 87.6 ms: 1.16x slower                                                    |
| nbody                    | 70.0 ms                                                     | 82.6 ms: 1.18x slower                                                    |
| pathlib                  | 71.4 ms                                                     | 85.1 ms: 1.19x slower                                                    |
| hexiom                   | 4.55 ms                                                     | 5.48 ms: 1.20x slower                                                    |
| fannkuch                 | 252 ms                                                      | 304 ms: 1.21x slower                                                     |
| tomli_loads              | 1.41 sec                                                    | 1.77 sec: 1.25x slower                                                   |
| telco                    | 3.90 ms                                                     | 4.89 ms: 1.25x slower                                                    |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 3.68 ms: 1.43x slower                                                    |
| async_generators         | 178 ms                                                      | 254 ms: 1.43x slower                                                     |
| dask                     | 264 ms                                                      | 397 ms: 1.50x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.04x slower                                                             |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, async_tree_io, pidigits, pickle_dict, mypy2, tornado_http
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
