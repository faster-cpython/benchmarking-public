
# Results vs. 3.11.0

- fork: python
- ref: 9564e31cbc95a723f241
- machine: windows-amd64
- commit hash: 9564e31
- commit date: 2023-08-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.72 sec: 1.07x slower                                                     |
| tornado_http   | 91.8 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| float          | 54.6 ms                                                     | 58.5 ms: 1.07x slower                                                      |
| nbody          | 70.0 ms                                                     | 82.5 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 95.6 ms: 1.06x slower                                                      |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.64 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.90 ms: 1.28x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 148 us: 1.03x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                                      |
| pickle_pure_python   | 200 us                                                      | 202 us: 1.01x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.34 us: 1.03x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.8 us: 1.07x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 67.3 ms: 1.08x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                                      |
| pickle_dict          | 18.5 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle               | 6.61 us                                                     | 7.32 us: 1.11x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.88 us: 1.13x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 59.1 ms: 1.13x slower                                                      |
| tomli_loads          | 1.41 sec                                                    | 1.66 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.94 ms: 1.09x slower                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 98.5 us: 3.27x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 501 ms: 1.39x faster                                                       |
| json_dumps               | 7.56 ms                                                     | 5.90 ms: 1.28x faster                                                      |
| generators               | 33.8 ms                                                     | 26.8 ms: 1.26x faster                                                      |
| unpack_sequence          | 46.1 ns                                                     | 38.5 ns: 1.20x faster                                                      |
| json                     | 3.25 ms                                                     | 2.87 ms: 1.13x faster                                                      |
| raytrace                 | 211 ms                                                      | 190 ms: 1.11x faster                                                       |
| deltablue                | 2.61 ms                                                     | 2.42 ms: 1.08x faster                                                      |
| richards_super           | 37.5 ms                                                     | 34.9 ms: 1.07x faster                                                      |
| mdp                      | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                     |
| coverage                 | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                                      |
| chaos                    | 47.1 ms                                                     | 44.6 ms: 1.06x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 910 us: 1.05x faster                                                       |
| mypy2                    | 229 ms                                                      | 222 ms: 1.03x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 148 us: 1.03x faster                                                       |
| xml_etree_parse          | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                                      |
| async_tree_none          | 320 ms                                                      | 313 ms: 1.02x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.14 ms: 1.02x faster                                                      |
| comprehensions           | 15.9 us                                                     | 15.6 us: 1.02x faster                                                      |
| logging_silent           | 69.8 ns                                                     | 68.9 ns: 1.01x faster                                                      |
| tornado_http             | 91.8 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| pidigits                 | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| scimark_lu               | 63.5 ms                                                     | 64.0 ms: 1.01x slower                                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.0 ms: 1.01x slower                                                      |
| richards                 | 30.6 ms                                                     | 30.8 ms: 1.01x slower                                                      |
| pickle_pure_python       | 200 us                                                      | 202 us: 1.01x slower                                                       |
| nqueens                  | 64.9 ms                                                     | 66.0 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.61 ms: 1.02x slower                                                      |
| hexiom                   | 4.55 ms                                                     | 4.64 ms: 1.02x slower                                                      |
| meteor_contest           | 74.7 ms                                                     | 76.9 ms: 1.03x slower                                                      |
| unpickle                 | 8.09 us                                                     | 8.34 us: 1.03x slower                                                      |
| fannkuch                 | 252 ms                                                      | 261 ms: 1.03x slower                                                       |
| sqlglot_normalize        | 190 ms                                                      | 198 ms: 1.04x slower                                                       |
| deepcopy_memo            | 25.2 us                                                     | 26.2 us: 1.04x slower                                                      |
| deepcopy                 | 246 us                                                      | 256 us: 1.04x slower                                                       |
| spectral_norm            | 67.9 ms                                                     | 70.9 ms: 1.04x slower                                                      |
| go                       | 97.3 ms                                                     | 102 ms: 1.05x slower                                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 36.5 ms: 1.05x slower                                                      |
| logging_simple           | 6.61 us                                                     | 6.93 us: 1.05x slower                                                      |
| python_startup           | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                                      |
| sqlite_synth             | 1.68 us                                                     | 1.77 us: 1.05x slower                                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                                      |
| regex_compile            | 90.6 ms                                                     | 95.6 ms: 1.06x slower                                                      |
| gc_traversal             | 1.46 ms                                                     | 1.54 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 512 ms                                                      | 543 ms: 1.06x slower                                                       |
| pickle_list              | 2.68 us                                                     | 2.84 us: 1.06x slower                                                      |
| regex_dna                | 115 ms                                                      | 123 ms: 1.06x slower                                                       |
| scimark_fft              | 178 ms                                                      | 190 ms: 1.06x slower                                                       |
| pyflate                  | 304 ms                                                      | 324 ms: 1.06x slower                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.11 sec: 1.07x slower                                                     |
| float                    | 54.6 ms                                                     | 58.5 ms: 1.07x slower                                                      |
| json_loads               | 12.9 us                                                     | 13.8 us: 1.07x slower                                                      |
| docutils                 | 1.60 sec                                                    | 1.72 sec: 1.07x slower                                                     |
| dulwich_log              | 44.5 ms                                                     | 47.7 ms: 1.07x slower                                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 67.3 ms: 1.08x slower                                                      |
| logging_format           | 7.01 us                                                     | 7.59 us: 1.08x slower                                                      |
| bench_mp_pool            | 62.5 ms                                                     | 67.9 ms: 1.09x slower                                                      |
| coroutines               | 14.6 ms                                                     | 15.9 ms: 1.09x slower                                                      |
| xml_etree_process        | 37.1 ms                                                     | 40.4 ms: 1.09x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 756 us: 1.09x slower                                                       |
| mako                     | 7.26 ms                                                     | 7.94 ms: 1.09x slower                                                      |
| regex_effbot             | 1.50 ms                                                     | 1.64 ms: 1.09x slower                                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.29 us: 1.10x slower                                                      |
| pickle_dict              | 18.5 us                                                     | 20.5 us: 1.11x slower                                                      |
| pickle                   | 6.61 us                                                     | 7.32 us: 1.11x slower                                                      |
| unpickle_list            | 2.55 us                                                     | 2.88 us: 1.13x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                     | 59.1 ms: 1.13x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 86.3 ms: 1.14x slower                                                      |
| tomli_loads              | 1.41 sec                                                    | 1.66 sec: 1.17x slower                                                     |
| pycparser                | 691 ms                                                      | 811 ms: 1.17x slower                                                       |
| nbody                    | 70.0 ms                                                     | 82.5 ms: 1.18x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 85.1 ms: 1.19x slower                                                      |
| telco                    | 3.90 ms                                                     | 4.80 ms: 1.23x slower                                                      |
| async_generators         | 178 ms                                                      | 252 ms: 1.42x slower                                                       |
| dask                     | 264 ms                                                      | 393 ms: 1.49x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, bench_thread_pool, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, crypto_pyaes, regex_v8
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
