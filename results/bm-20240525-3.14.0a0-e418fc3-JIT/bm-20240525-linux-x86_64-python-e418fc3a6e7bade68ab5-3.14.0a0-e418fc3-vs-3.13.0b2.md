# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x faster
- HPT reliability: 75.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| chameleon      | 7.22 ms                                                    | 7.04 ms: 1.02x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                |
| html5lib       | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 97.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                 |
| float          | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.07x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.02x faster                                                  |
| pickle_list          | 5.11 us                                                    | 5.07 us: 1.01x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 224 us: 1.03x slower                                                  |
| pickle_dict          | 34.8 us                                                    | 35.9 us: 1.03x slower                                                 |
| pickle               | 11.5 us                                                    | 11.9 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): unpickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                 |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 309 ms: 1.27x faster                                                  |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                                 |
| richards                 | 50.9 ms                                                    | 41.7 ms: 1.22x faster                                                 |
| richards_super           | 57.4 ms                                                    | 48.0 ms: 1.20x faster                                                 |
| spectral_norm            | 116 ms                                                     | 100 ms: 1.16x faster                                                  |
| crypto_pyaes             | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                 |
| mako                     | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                 |
| fannkuch                 | 402 ms                                                     | 356 ms: 1.13x faster                                                  |
| scimark_monte_carlo      | 69.2 ms                                                    | 62.1 ms: 1.11x faster                                                 |
| nbody                    | 88.3 ms                                                    | 80.8 ms: 1.09x faster                                                 |
| float                    | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                                 |
| mdp                      | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                |
| xml_etree_parse          | 162 ms                                                     | 150 ms: 1.08x faster                                                  |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.07x faster                                                  |
| xml_etree_generate       | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                 |
| pyflate                  | 484 ms                                                     | 455 ms: 1.06x faster                                                  |
| xml_etree_process        | 61.2 ms                                                    | 57.8 ms: 1.06x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.86 us: 1.05x faster                                                 |
| pprint_safe_repr         | 758 ms                                                     | 725 ms: 1.05x faster                                                  |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| telco                    | 8.41 ms                                                    | 8.12 ms: 1.04x faster                                                 |
| gc_traversal             | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.29 us: 1.03x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 38.6 us: 1.03x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.04 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| pickle_pure_python       | 305 us                                                     | 301 us: 1.02x faster                                                  |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.01x faster                                                  |
| logging_simple           | 5.74 us                                                    | 5.67 us: 1.01x faster                                                 |
| coroutines               | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| thrift                   | 823 us                                                     | 816 us: 1.01x faster                                                  |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                 |
| pickle_list              | 5.11 us                                                    | 5.07 us: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.63 ms: 1.01x faster                                                 |
| scimark_lu               | 122 ms                                                     | 122 ms: 1.01x slower                                                  |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| bench_mp_pool            | 23.9 ms                                                    | 24.1 ms: 1.01x slower                                                 |
| coverage                 | 93.1 ms                                                    | 94.0 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                |
| create_gc_cycles         | 1.82 ms                                                    | 1.84 ms: 1.01x slower                                                 |
| regex_effbot             | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| html5lib                 | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                 |
| sqlglot_optimize         | 55.5 ms                                                    | 56.4 ms: 1.01x slower                                                 |
| dask                     | 369 ms                                                     | 376 ms: 1.02x slower                                                  |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| flaskblogging            | 9.01 ms                                                    | 9.20 ms: 1.02x slower                                                 |
| asyncio_tcp              | 508 ms                                                     | 520 ms: 1.02x slower                                                  |
| tornado_http             | 94.6 ms                                                    | 97.0 ms: 1.03x slower                                                 |
| generators               | 29.6 ms                                                    | 30.4 ms: 1.03x slower                                                 |
| go                       | 145 ms                                                     | 148 ms: 1.03x slower                                                  |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                 |
| unpickle_pure_python     | 218 us                                                     | 224 us: 1.03x slower                                                  |
| pickle_dict              | 34.8 us                                                    | 35.9 us: 1.03x slower                                                 |
| sqlglot_normalize        | 110 ms                                                     | 114 ms: 1.03x slower                                                  |
| logging_silent           | 105 ns                                                     | 108 ns: 1.03x slower                                                  |
| dulwich_log              | 67.2 ms                                                    | 69.3 ms: 1.03x slower                                                 |
| django_template          | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                 |
| regex_dna                | 221 ms                                                     | 229 ms: 1.04x slower                                                  |
| bench_thread_pool        | 834 us                                                     | 867 us: 1.04x slower                                                  |
| pickle                   | 11.5 us                                                    | 11.9 us: 1.04x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.56 ms: 1.04x slower                                                 |
| docutils                 | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                |
| raytrace                 | 267 ms                                                     | 278 ms: 1.04x slower                                                  |
| async_generators         | 442 ms                                                     | 462 ms: 1.05x slower                                                  |
| typing_runtime_protocols | 165 us                                                     | 173 us: 1.05x slower                                                  |
| pycparser                | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                                |
| genshi_text              | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                 |
| nqueens                  | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                 |
| python_startup_no_site   | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| sympy_str                | 282 ms                                                     | 303 ms: 1.07x slower                                                  |
| sympy_expand             | 473 ms                                                     | 509 ms: 1.08x slower                                                  |
| scimark_sor              | 127 ms                                                     | 138 ms: 1.08x slower                                                  |
| sympy_sum                | 156 ms                                                     | 171 ms: 1.10x slower                                                  |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| genshi_xml               | 51.6 ms                                                    | 57.4 ms: 1.11x slower                                                 |
| pylint                   | 317 ms                                                     | 353 ms: 1.11x slower                                                  |
| deltablue                | 3.25 ms                                                    | 3.72 ms: 1.14x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (17): async_tree_none_tg, deepcopy, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, deepcopy_reduce, comprehensions, unpickle_list, regex_v8, json_loads, json, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, unpickle
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 75.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x