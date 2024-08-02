# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| chameleon      | 7.22 ms                                                    | 7.01 ms: 1.03x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| tornado_http   | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg | 336 ms                                                     | 352 ms: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 84.6 ms: 1.04x faster                                                 |
| float          | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                 |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                 |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                |
| pickle_list          | 5.11 us                                                    | 5.20 us: 1.02x slower                                                 |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| pickle_dict          | 34.8 us                                                    | 35.7 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (3): unpickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 51.3 ms: 1.01x faster                                                 |
| django_template | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 359 ms: 1.09x faster                                                  |
| scimark_lu               | 122 ms                                                     | 113 ms: 1.07x faster                                                  |
| pathlib                  | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                 |
| richards_super           | 57.4 ms                                                    | 54.8 ms: 1.05x faster                                                 |
| richards                 | 50.9 ms                                                    | 48.6 ms: 1.05x faster                                                 |
| gc_traversal             | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                 |
| nbody                    | 88.3 ms                                                    | 84.6 ms: 1.04x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 74.4 ms: 1.04x faster                                                 |
| logging_silent           | 105 ns                                                     | 101 ns: 1.04x faster                                                  |
| generators               | 29.6 ms                                                    | 28.6 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.09 ms: 1.04x faster                                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 67.0 ms: 1.03x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.01 ms: 1.03x faster                                                 |
| hexiom                   | 6.30 ms                                                    | 6.12 ms: 1.03x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.52 sec: 1.03x faster                                                |
| spectral_norm            | 116 ms                                                     | 113 ms: 1.03x faster                                                  |
| pyflate                  | 484 ms                                                     | 472 ms: 1.03x faster                                                  |
| pprint_safe_repr         | 758 ms                                                     | 741 ms: 1.02x faster                                                  |
| float                    | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                 |
| dulwich_log              | 67.2 ms                                                    | 65.7 ms: 1.02x faster                                                 |
| thrift                   | 823 us                                                     | 805 us: 1.02x faster                                                  |
| deepcopy_reduce          | 3.35 us                                                    | 3.28 us: 1.02x faster                                                 |
| coverage                 | 93.1 ms                                                    | 91.1 ms: 1.02x faster                                                 |
| mako                     | 11.2 ms                                                    | 11.0 ms: 1.02x faster                                                 |
| xml_etree_process        | 61.2 ms                                                    | 59.9 ms: 1.02x faster                                                 |
| fannkuch                 | 402 ms                                                     | 394 ms: 1.02x faster                                                  |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                  |
| unpickle_pure_python     | 218 us                                                     | 214 us: 1.02x faster                                                  |
| deepcopy_memo            | 39.7 us                                                    | 39.0 us: 1.02x faster                                                 |
| regex_compile            | 137 ms                                                     | 134 ms: 1.02x faster                                                  |
| create_gc_cycles         | 1.82 ms                                                    | 1.79 ms: 1.02x faster                                                 |
| xml_etree_parse          | 162 ms                                                     | 159 ms: 1.02x faster                                                  |
| chaos                    | 61.3 ms                                                    | 60.4 ms: 1.02x faster                                                 |
| raytrace                 | 267 ms                                                     | 262 ms: 1.02x faster                                                  |
| python_startup           | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                 |
| docutils                 | 2.83 sec                                                   | 2.78 sec: 1.02x faster                                                |
| xml_etree_iterparse      | 107 ms                                                     | 106 ms: 1.01x faster                                                  |
| xml_etree_generate       | 87.4 ms                                                    | 86.2 ms: 1.01x faster                                                 |
| regex_v8                 | 25.1 ms                                                    | 24.8 ms: 1.01x faster                                                 |
| mdp                      | 2.79 sec                                                   | 2.76 sec: 1.01x faster                                                |
| 2to3                     | 274 ms                                                     | 271 ms: 1.01x faster                                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 55.0 ms: 1.01x faster                                                 |
| deepcopy                 | 367 us                                                     | 364 us: 1.01x faster                                                  |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.01x faster                                                  |
| sympy_sum                | 156 ms                                                     | 154 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                     | 190 ms: 1.01x faster                                                  |
| comprehensions           | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| tornado_http             | 94.6 ms                                                    | 93.9 ms: 1.01x faster                                                 |
| genshi_xml               | 51.6 ms                                                    | 51.3 ms: 1.01x faster                                                 |
| sympy_integrate          | 20.5 ms                                                    | 20.4 ms: 1.01x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.43 us: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.63 ms: 1.01x faster                                                 |
| json                     | 5.31 ms                                                    | 5.28 ms: 1.01x faster                                                 |
| bench_thread_pool        | 834 us                                                     | 830 us: 1.00x faster                                                  |
| go                       | 145 ms                                                     | 144 ms: 1.00x faster                                                  |
| python_startup_no_site   | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                 |
| regex_dna                | 221 ms                                                     | 222 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                |
| nqueens                  | 81.4 ms                                                    | 81.8 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                 |
| coroutines               | 23.2 ms                                                    | 23.4 ms: 1.01x slower                                                 |
| logging_simple           | 5.74 us                                                    | 5.80 us: 1.01x slower                                                 |
| typing_runtime_protocols | 165 us                                                     | 166 us: 1.01x slower                                                  |
| json_dumps               | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                 |
| tomli_loads              | 2.12 sec                                                   | 2.15 sec: 1.01x slower                                                |
| django_template          | 34.8 ms                                                    | 35.3 ms: 1.01x slower                                                 |
| pickle_list              | 5.11 us                                                    | 5.20 us: 1.02x slower                                                 |
| telco                    | 8.41 ms                                                    | 8.59 ms: 1.02x slower                                                 |
| regex_effbot             | 3.67 ms                                                    | 3.75 ms: 1.02x slower                                                 |
| async_generators         | 442 ms                                                     | 452 ms: 1.02x slower                                                  |
| pickle                   | 11.5 us                                                    | 11.7 us: 1.02x slower                                                 |
| pickle_dict              | 34.8 us                                                    | 35.7 us: 1.03x slower                                                 |
| scimark_sor              | 127 ms                                                     | 133 ms: 1.04x slower                                                  |
| async_tree_none_tg       | 336 ms                                                     | 352 ms: 1.05x slower                                                  |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (24): flaskblogging, sympy_str, dask, sqlite_synth, html5lib, sqlglot_normalize, asyncio_websockets, asyncio_tcp, unpickle_list, json_loads, async_tree_memoization, pylint, deltablue, pycparser, async_tree_cpu_io_mixed_tg, genshi_text, sympy_expand, bench_mp_pool, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, unpickle, async_tree_memoization_tg, async_tree_io_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x