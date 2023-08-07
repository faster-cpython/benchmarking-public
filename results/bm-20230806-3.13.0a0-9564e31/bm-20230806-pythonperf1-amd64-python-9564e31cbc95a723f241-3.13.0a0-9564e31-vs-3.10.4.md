
# Results vs. 3.10.4

- fork: python
- ref: 9564e31cbc95a723f241
- machine: windows-amd64
- commit hash: 9564e31
- commit date: 2023-08-06
- overall geometric mean: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.72 sec: 1.10x faster                                                     |
| tornado_http   | 109 ms                                                      | 91.0 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 58.5 ms: 1.03x faster                                                      |
| pidigits       | 145 ms                                                      | 147 ms: 1.02x slower                                                       |
| nbody          | 69.3 ms                                                     | 82.5 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 95.6 ms: 1.08x faster                                                      |
| regex_dna      | 132 ms                                                      | 123 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.90 ms: 1.44x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 202 us: 1.27x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 148 us: 1.16x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.34 us: 1.10x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 93.8 ms: 1.09x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.8 us: 1.03x faster                                                      |
| tomli_loads          | 1.62 sec                                                    | 1.66 sec: 1.02x slower                                                     |
| unpickle_list        | 2.81 us                                                     | 2.88 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 67.3 ms: 1.06x slower                                                      |
| pickle               | 6.80 us                                                     | 7.32 us: 1.08x slower                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 59.1 ms: 1.08x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 20.5 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.94 ms: 1.11x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 98.5 us: 3.30x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.42 ms: 1.72x faster                                                      |
| mypy2                    | 352 ms                                                      | 222 ms: 1.58x faster                                                       |
| richards_super           | 51.7 ms                                                     | 34.9 ms: 1.48x faster                                                      |
| json_dumps               | 8.50 ms                                                     | 5.90 ms: 1.44x faster                                                      |
| raytrace                 | 271 ms                                                      | 190 ms: 1.43x faster                                                       |
| asyncio_tcp              | 712 ms                                                      | 501 ms: 1.42x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 68.9 ns: 1.40x faster                                                      |
| async_tree_io            | 1.07 sec                                                    | 774 ms: 1.38x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 367 ms: 1.35x faster                                                       |
| async_tree_none          | 420 ms                                                      | 313 ms: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 910 us: 1.34x faster                                                       |
| richards                 | 41.2 ms                                                     | 30.8 ms: 1.34x faster                                                      |
| go                       | 136 ms                                                      | 102 ms: 1.34x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 64.0 ms: 1.34x faster                                                      |
| chaos                    | 58.9 ms                                                     | 44.6 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 47.7 ms: 1.31x faster                                                      |
| sqlglot_transpile        | 1.46 ms                                                     | 1.14 ms: 1.28x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 202 us: 1.27x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 45.0 ms: 1.24x faster                                                      |
| scimark_sor              | 105 ms                                                      | 86.3 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 502 ms: 1.21x faster                                                       |
| tornado_http             | 109 ms                                                      | 91.0 ms: 1.20x faster                                                      |
| pyflate                  | 387 ms                                                      | 324 ms: 1.19x faster                                                       |
| hexiom                   | 5.52 ms                                                     | 4.64 ms: 1.19x faster                                                      |
| generators               | 31.6 ms                                                     | 26.8 ms: 1.18x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 148 us: 1.16x faster                                                       |
| bench_thread_pool        | 946 us                                                      | 842 us: 1.12x faster                                                       |
| mako                     | 8.80 ms                                                     | 7.94 ms: 1.11x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.72 sec: 1.10x faster                                                     |
| spectral_norm            | 78.0 ms                                                     | 70.9 ms: 1.10x faster                                                      |
| unpickle                 | 9.17 us                                                     | 8.34 us: 1.10x faster                                                      |
| mdp                      | 1.71 sec                                                    | 1.56 sec: 1.10x faster                                                     |
| deepcopy_memo            | 28.5 us                                                     | 26.2 us: 1.09x faster                                                      |
| pprint_pformat           | 1.21 sec                                                    | 1.11 sec: 1.09x faster                                                     |
| pprint_safe_repr         | 589 ms                                                      | 543 ms: 1.09x faster                                                       |
| xml_etree_parse          | 102 ms                                                      | 93.8 ms: 1.09x faster                                                      |
| regex_compile            | 103 ms                                                      | 95.6 ms: 1.08x faster                                                      |
| xml_etree_process        | 43.4 ms                                                     | 40.4 ms: 1.08x faster                                                      |
| regex_dna                | 132 ms                                                      | 123 ms: 1.08x faster                                                       |
| pycparser                | 868 ms                                                      | 811 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 36.5 ms: 1.07x faster                                                      |
| json                     | 3.05 ms                                                     | 2.87 ms: 1.06x faster                                                      |
| sqlite_synth             | 1.84 us                                                     | 1.77 us: 1.04x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 756 us: 1.03x faster                                                       |
| float                    | 60.2 ms                                                     | 58.5 ms: 1.03x faster                                                      |
| json_loads               | 14.2 us                                                     | 13.8 us: 1.03x faster                                                      |
| comprehensions           | 16.0 us                                                     | 15.6 us: 1.02x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 198 ms: 1.02x faster                                                       |
| python_startup           | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                                      |
| scimark_fft              | 193 ms                                                      | 190 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.61 ms: 1.02x faster                                                      |
| nqueens                  | 67.0 ms                                                     | 66.0 ms: 1.02x faster                                                      |
| fannkuch                 | 258 ms                                                      | 261 ms: 1.01x slower                                                       |
| pidigits                 | 145 ms                                                      | 147 ms: 1.02x slower                                                       |
| unpack_sequence          | 37.8 ns                                                     | 38.5 ns: 1.02x slower                                                      |
| tomli_loads              | 1.62 sec                                                    | 1.66 sec: 1.02x slower                                                     |
| unpickle_list            | 2.81 us                                                     | 2.88 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 67.3 ms: 1.06x slower                                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.29 us: 1.06x slower                                                      |
| meteor_contest           | 72.5 ms                                                     | 76.9 ms: 1.06x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.32 us: 1.08x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 59.1 ms: 1.08x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.84 us: 1.10x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 85.1 ms: 1.10x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.93 us: 1.12x slower                                                      |
| bench_mp_pool            | 60.7 ms                                                     | 67.9 ms: 1.12x slower                                                      |
| async_generators         | 224 ms                                                      | 252 ms: 1.13x slower                                                       |
| logging_format           | 6.66 us                                                     | 7.59 us: 1.14x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.54 ms: 1.15x slower                                                      |
| nbody                    | 69.3 ms                                                     | 82.5 ms: 1.19x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 20.5 us: 1.21x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.80 ms: 1.27x slower                                                      |
| dask                     | 305 ms                                                      | 393 ms: 1.29x slower                                                       |
| coverage                 | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (5): regex_v8, coroutines, deepcopy, dulwich_log, asyncio_tcp_ssl
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
