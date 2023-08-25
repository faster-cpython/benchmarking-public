
# Results vs. 3.11.0

- fork: python
- ref: 9564e31cbc95a723f241
- machine: windows-amd64
- commit hash: 9564e31
- commit date: 2023-08-06
- overall geometric mean: 1.01x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.71 sec: 1.07x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| float          | 54.6 ms                                                     | 58.7 ms: 1.08x slower                                                      |
| nbody          | 70.0 ms                                                     | 82.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| regex_compile  | 90.6 ms                                                     | 96.4 ms: 1.06x slower                                                      |
| regex_effbot   | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.80 ms: 1.30x faster                                                      |
| unpickle_pure_python | 152 us                                                      | 150 us: 1.01x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 204 us: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                                      |
| unpickle             | 8.09 us                                                     | 8.45 us: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                                      |
| json_loads           | 12.9 us                                                     | 13.9 us: 1.08x slower                                                      |
| xml_etree_process    | 37.1 ms                                                     | 40.8 ms: 1.10x slower                                                      |
| unpickle_list        | 2.55 us                                                     | 2.81 us: 1.10x slower                                                      |
| pickle               | 6.61 us                                                     | 7.39 us: 1.12x slower                                                      |
| xml_etree_generate   | 52.2 ms                                                     | 59.0 ms: 1.13x slower                                                      |
| tomli_loads          | 1.41 sec                                                    | 1.65 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                      |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 8.01 ms: 1.10x slower                                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.5 us: 3.30x faster                                                      |
| asyncio_tcp              | 699 ms                                                      | 505 ms: 1.38x faster                                                       |
| json_dumps               | 7.56 ms                                                     | 5.80 ms: 1.30x faster                                                      |
| generators               | 33.8 ms                                                     | 27.5 ms: 1.23x faster                                                      |
| unpack_sequence          | 46.1 ns                                                     | 38.4 ns: 1.20x faster                                                      |
| json                     | 3.25 ms                                                     | 2.85 ms: 1.14x faster                                                      |
| mdp                      | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                     |
| deltablue                | 2.61 ms                                                     | 2.41 ms: 1.08x faster                                                      |
| raytrace                 | 211 ms                                                      | 195 ms: 1.08x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.97 sec: 1.07x faster                                                     |
| richards_super           | 37.5 ms                                                     | 34.9 ms: 1.07x faster                                                      |
| coverage                 | 55.9 ms                                                     | 52.2 ms: 1.07x faster                                                      |
| chaos                    | 47.1 ms                                                     | 44.6 ms: 1.06x faster                                                      |
| sqlglot_parse            | 952 us                                                      | 918 us: 1.04x faster                                                       |
| async_tree_none          | 320 ms                                                      | 313 ms: 1.02x faster                                                       |
| regex_v8                 | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                      |
| async_tree_io            | 779 ms                                                      | 767 ms: 1.01x faster                                                       |
| mypy2                    | 229 ms                                                      | 226 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 152 us                                                      | 150 us: 1.01x faster                                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.15 ms: 1.01x faster                                                      |
| logging_silent           | 69.8 ns                                                     | 69.1 ns: 1.01x faster                                                      |
| crypto_pyaes             | 47.6 ms                                                     | 47.1 ms: 1.01x faster                                                      |
| scimark_lu               | 63.5 ms                                                     | 63.0 ms: 1.01x faster                                                      |
| comprehensions           | 15.9 us                                                     | 15.8 us: 1.01x faster                                                      |
| pidigits                 | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| meteor_contest           | 74.7 ms                                                     | 75.4 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.60 ms: 1.01x slower                                                      |
| spectral_norm            | 67.9 ms                                                     | 68.8 ms: 1.01x slower                                                      |
| richards                 | 30.6 ms                                                     | 31.1 ms: 1.02x slower                                                      |
| hexiom                   | 4.55 ms                                                     | 4.64 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 510 ms: 1.02x slower                                                       |
| pickle_pure_python       | 200 us                                                      | 204 us: 1.02x slower                                                       |
| python_startup_no_site   | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                      |
| deepcopy_memo            | 25.2 us                                                     | 25.7 us: 1.02x slower                                                      |
| deepcopy                 | 246 us                                                      | 252 us: 1.02x slower                                                       |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                      |
| pickle_dict              | 18.5 us                                                     | 19.1 us: 1.03x slower                                                      |
| go                       | 97.3 ms                                                     | 101 ms: 1.03x slower                                                       |
| fannkuch                 | 252 ms                                                      | 262 ms: 1.04x slower                                                       |
| unpickle                 | 8.09 us                                                     | 8.45 us: 1.04x slower                                                      |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                                      |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.05x slower                                                      |
| sqlglot_normalize        | 190 ms                                                      | 200 ms: 1.05x slower                                                       |
| dulwich_log              | 44.5 ms                                                     | 46.9 ms: 1.05x slower                                                      |
| regex_dna                | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| scimark_fft              | 178 ms                                                      | 189 ms: 1.06x slower                                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 66.3 ms: 1.06x slower                                                      |
| pickle_list              | 2.68 us                                                     | 2.84 us: 1.06x slower                                                      |
| regex_compile            | 90.6 ms                                                     | 96.4 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 512 ms                                                      | 544 ms: 1.06x slower                                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 37.1 ms: 1.06x slower                                                      |
| docutils                 | 1.60 sec                                                    | 1.71 sec: 1.07x slower                                                     |
| float                    | 54.6 ms                                                     | 58.7 ms: 1.08x slower                                                      |
| pyflate                  | 304 ms                                                      | 327 ms: 1.08x slower                                                       |
| json_loads               | 12.9 us                                                     | 13.9 us: 1.08x slower                                                      |
| logging_simple           | 6.61 us                                                     | 7.12 us: 1.08x slower                                                      |
| bench_mp_pool            | 62.5 ms                                                     | 67.7 ms: 1.08x slower                                                      |
| create_gc_cycles         | 693 us                                                      | 750 us: 1.08x slower                                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.13 sec: 1.09x slower                                                     |
| deepcopy_reduce          | 2.07 us                                                     | 2.25 us: 1.09x slower                                                      |
| logging_format           | 7.01 us                                                     | 7.65 us: 1.09x slower                                                      |
| xml_etree_process        | 37.1 ms                                                     | 40.8 ms: 1.10x slower                                                      |
| regex_effbot             | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                      |
| mako                     | 7.26 ms                                                     | 8.01 ms: 1.10x slower                                                      |
| unpickle_list            | 2.55 us                                                     | 2.81 us: 1.10x slower                                                      |
| pickle                   | 6.61 us                                                     | 7.39 us: 1.12x slower                                                      |
| coroutines               | 14.6 ms                                                     | 16.5 ms: 1.13x slower                                                      |
| xml_etree_generate       | 52.2 ms                                                     | 59.0 ms: 1.13x slower                                                      |
| scimark_sor              | 75.6 ms                                                     | 86.9 ms: 1.15x slower                                                      |
| pycparser                | 691 ms                                                      | 802 ms: 1.16x slower                                                       |
| tomli_loads              | 1.41 sec                                                    | 1.65 sec: 1.17x slower                                                     |
| nbody                    | 70.0 ms                                                     | 82.2 ms: 1.17x slower                                                      |
| pathlib                  | 71.4 ms                                                     | 83.9 ms: 1.18x slower                                                      |
| telco                    | 3.90 ms                                                     | 4.72 ms: 1.21x slower                                                      |
| async_generators         | 178 ms                                                      | 248 ms: 1.40x slower                                                       |
| dask                     | 264 ms                                                      | 394 ms: 1.49x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (6): xml_etree_parse, nqueens, tornado_http, scimark_monte_carlo, async_tree_memoization, bench_thread_pool
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
