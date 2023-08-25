
# Results vs. 3.10.4

- fork: python
- ref: 9564e31cbc95a723f241
- machine: windows-amd64
- commit hash: 9564e31
- commit date: 2023-08-06
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.71 sec: 1.11x faster                                                     |
| tornado_http   | 109 ms                                                      | 91.8 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 58.7 ms: 1.03x faster                                                      |
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                                       |
| nbody          | 69.3 ms                                                     | 82.2 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                                      |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                                       |
| regex_compile  | 103 ms                                                      | 96.4 ms: 1.07x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.80 ms: 1.47x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 150 us: 1.14x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.45 us: 1.09x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 95.5 ms: 1.07x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 40.8 ms: 1.07x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                                      |
| tomli_loads          | 1.62 sec                                                    | 1.65 sec: 1.02x slower                                                     |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.3 ms: 1.04x slower                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 59.0 ms: 1.08x slower                                                      |
| pickle               | 6.80 us                                                     | 7.39 us: 1.09x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 8.01 ms: 1.10x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 97.5 us: 3.33x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.41 ms: 1.73x faster                                                      |
| mypy2                    | 352 ms                                                      | 226 ms: 1.56x faster                                                       |
| richards_super           | 51.7 ms                                                     | 34.9 ms: 1.48x faster                                                      |
| json_dumps               | 8.50 ms                                                     | 5.80 ms: 1.47x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 505 ms: 1.41x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 69.1 ns: 1.39x faster                                                      |
| raytrace                 | 271 ms                                                      | 195 ms: 1.39x faster                                                       |
| async_tree_io            | 1.07 sec                                                    | 767 ms: 1.39x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 63.0 ms: 1.36x faster                                                      |
| go                       | 136 ms                                                      | 101 ms: 1.35x faster                                                       |
| async_tree_none          | 420 ms                                                      | 313 ms: 1.34x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 372 ms: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 918 us: 1.33x faster                                                       |
| richards                 | 41.2 ms                                                     | 31.1 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 47.1 ms: 1.32x faster                                                      |
| chaos                    | 58.9 ms                                                     | 44.6 ms: 1.32x faster                                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.15 ms: 1.27x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 204 us: 1.26x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 44.8 ms: 1.25x faster                                                      |
| scimark_sor              | 105 ms                                                      | 86.9 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 510 ms: 1.19x faster                                                       |
| hexiom                   | 5.52 ms                                                     | 4.64 ms: 1.19x faster                                                      |
| tornado_http             | 109 ms                                                      | 91.8 ms: 1.19x faster                                                      |
| pyflate                  | 387 ms                                                      | 327 ms: 1.18x faster                                                       |
| mdp                      | 1.71 sec                                                    | 1.46 sec: 1.17x faster                                                     |
| generators               | 31.6 ms                                                     | 27.5 ms: 1.15x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 150 us: 1.14x faster                                                       |
| spectral_norm            | 78.0 ms                                                     | 68.8 ms: 1.13x faster                                                      |
| deepcopy_memo            | 28.5 us                                                     | 25.7 us: 1.11x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.71 sec: 1.11x faster                                                     |
| regex_v8                 | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                                      |
| bench_thread_pool        | 946 us                                                      | 860 us: 1.10x faster                                                       |
| mako                     | 8.80 ms                                                     | 8.01 ms: 1.10x faster                                                      |
| unpickle                 | 9.17 us                                                     | 8.45 us: 1.09x faster                                                      |
| pycparser                | 868 ms                                                      | 802 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 589 ms                                                      | 544 ms: 1.08x faster                                                       |
| regex_dna                | 132 ms                                                      | 122 ms: 1.08x faster                                                       |
| regex_compile            | 103 ms                                                      | 96.4 ms: 1.07x faster                                                      |
| json                     | 3.05 ms                                                     | 2.85 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.13 sec: 1.07x faster                                                     |
| xml_etree_parse          | 102 ms                                                      | 95.5 ms: 1.07x faster                                                      |
| xml_etree_process        | 43.4 ms                                                     | 40.8 ms: 1.07x faster                                                      |
| sqlglot_optimize         | 39.0 ms                                                     | 37.1 ms: 1.05x faster                                                      |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.04x faster                                                      |
| python_startup           | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 750 us: 1.04x faster                                                       |
| nqueens                  | 67.0 ms                                                     | 64.6 ms: 1.04x faster                                                      |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.97 sec: 1.03x faster                                                     |
| float                    | 60.2 ms                                                     | 58.7 ms: 1.03x faster                                                      |
| scimark_fft              | 193 ms                                                      | 189 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.60 ms: 1.02x faster                                                      |
| json_loads               | 14.2 us                                                     | 13.9 us: 1.02x faster                                                      |
| dulwich_log              | 47.6 ms                                                     | 46.9 ms: 1.01x faster                                                      |
| deepcopy                 | 255 us                                                      | 252 us: 1.01x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                      |
| comprehensions           | 16.0 us                                                     | 15.8 us: 1.01x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 200 ms: 1.01x faster                                                       |
| fannkuch                 | 258 ms                                                      | 262 ms: 1.02x slower                                                       |
| unpack_sequence          | 37.8 ns                                                     | 38.4 ns: 1.02x slower                                                      |
| tomli_loads              | 1.62 sec                                                    | 1.65 sec: 1.02x slower                                                     |
| pidigits                 | 145 ms                                                      | 149 ms: 1.03x slower                                                       |
| coroutines               | 15.9 ms                                                     | 16.5 ms: 1.04x slower                                                      |
| meteor_contest           | 72.5 ms                                                     | 75.4 ms: 1.04x slower                                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.3 ms: 1.04x slower                                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.25 us: 1.04x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.2 ms: 1.05x slower                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 59.0 ms: 1.08x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 83.9 ms: 1.08x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.39 us: 1.09x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.84 us: 1.10x slower                                                      |
| async_generators         | 224 ms                                                      | 248 ms: 1.11x slower                                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.7 ms: 1.11x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 19.1 us: 1.13x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.53 ms: 1.13x slower                                                      |
| logging_format           | 6.66 us                                                     | 7.65 us: 1.15x slower                                                      |
| logging_simple           | 6.20 us                                                     | 7.12 us: 1.15x slower                                                      |
| nbody                    | 69.3 ms                                                     | 82.2 ms: 1.19x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.72 ms: 1.25x slower                                                      |
| dask                     | 305 ms                                                      | 394 ms: 1.29x slower                                                       |
| coverage                 | 40.0 ms                                                     | 52.2 ms: 1.30x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x
