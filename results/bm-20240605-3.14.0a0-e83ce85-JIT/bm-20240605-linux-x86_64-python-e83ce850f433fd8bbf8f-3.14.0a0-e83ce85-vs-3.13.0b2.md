# Results vs. 3.13.0b2

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-x86_64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.01x faster
- HPT reliability: 73.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                |
| tornado_http   | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg        | 936 ms                                                     | 907 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed | 611 ms                                                     | 635 ms: 1.04x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                 |
| nbody          | 88.3 ms                                                    | 81.6 ms: 1.08x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                 |
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                |
| xml_etree_generate   | 87.4 ms                                                    | 81.2 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                                 |
| json_loads           | 28.9 us                                                    | 29.2 us: 1.01x slower                                                 |
| unpickle_pure_python | 218 us                                                     | 223 us: 1.02x slower                                                  |
| pickle_dict          | 34.8 us                                                    | 36.4 us: 1.05x slower                                                 |
| pickle               | 11.5 us                                                    | 12.1 us: 1.05x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.40 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.95 ms: 1.13x faster                                                 |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 318 ms: 1.23x faster                                                  |
| richards                 | 50.9 ms                                                    | 41.5 ms: 1.23x faster                                                 |
| richards_super           | 57.4 ms                                                    | 47.8 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.64 ms: 1.14x faster                                                 |
| fannkuch                 | 402 ms                                                     | 354 ms: 1.13x faster                                                  |
| crypto_pyaes             | 77.5 ms                                                    | 68.4 ms: 1.13x faster                                                 |
| spectral_norm            | 116 ms                                                     | 103 ms: 1.13x faster                                                  |
| mako                     | 11.2 ms                                                    | 9.95 ms: 1.13x faster                                                 |
| gc_traversal             | 3.98 ms                                                    | 3.60 ms: 1.11x faster                                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.2 ms: 1.09x faster                                                 |
| float                    | 78.9 ms                                                    | 72.6 ms: 1.09x faster                                                 |
| mdp                      | 2.79 sec                                                   | 2.57 sec: 1.09x faster                                                |
| xml_etree_parse          | 162 ms                                                     | 149 ms: 1.08x faster                                                  |
| tomli_loads              | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                |
| nbody                    | 88.3 ms                                                    | 81.6 ms: 1.08x faster                                                 |
| xml_etree_generate       | 87.4 ms                                                    | 81.2 ms: 1.08x faster                                                 |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                |
| pyflate                  | 484 ms                                                     | 453 ms: 1.07x faster                                                  |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| pprint_safe_repr         | 758 ms                                                     | 714 ms: 1.06x faster                                                  |
| pathlib                  | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.83 us: 1.06x faster                                                 |
| xml_etree_process        | 61.2 ms                                                    | 58.3 ms: 1.05x faster                                                 |
| json_dumps               | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                                 |
| async_tree_io_tg         | 936 ms                                                     | 907 ms: 1.03x faster                                                  |
| telco                    | 8.41 ms                                                    | 8.17 ms: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.29 us: 1.03x faster                                                 |
| meteor_contest           | 110 ms                                                     | 108 ms: 1.02x faster                                                  |
| coroutines               | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                 |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| create_gc_cycles         | 1.82 ms                                                    | 1.79 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.30 ms: 1.01x faster                                                 |
| unpickle_list            | 5.34 us                                                    | 5.30 us: 1.01x faster                                                 |
| regex_v8                 | 25.1 ms                                                    | 24.9 ms: 1.01x faster                                                 |
| asyncio_tcp              | 508 ms                                                     | 505 ms: 1.01x faster                                                  |
| thrift                   | 823 us                                                     | 817 us: 1.01x faster                                                  |
| comprehensions           | 16.6 us                                                    | 16.7 us: 1.01x slower                                                 |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                |
| deepcopy                 | 367 us                                                     | 370 us: 1.01x slower                                                  |
| coverage                 | 93.1 ms                                                    | 93.9 ms: 1.01x slower                                                 |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                  |
| regex_compile            | 137 ms                                                     | 138 ms: 1.01x slower                                                  |
| json_loads               | 28.9 us                                                    | 29.2 us: 1.01x slower                                                 |
| deepcopy_reduce          | 3.35 us                                                    | 3.41 us: 1.02x slower                                                 |
| 2to3                     | 274 ms                                                     | 279 ms: 1.02x slower                                                  |
| unpickle_pure_python     | 218 us                                                     | 223 us: 1.02x slower                                                  |
| dask                     | 369 ms                                                     | 378 ms: 1.02x slower                                                  |
| tornado_http             | 94.6 ms                                                    | 97.1 ms: 1.03x slower                                                 |
| json                     | 5.31 ms                                                    | 5.45 ms: 1.03x slower                                                 |
| sqlglot_optimize         | 55.5 ms                                                    | 57.1 ms: 1.03x slower                                                 |
| sqlglot_normalize        | 110 ms                                                     | 113 ms: 1.03x slower                                                  |
| dulwich_log              | 67.2 ms                                                    | 69.1 ms: 1.03x slower                                                 |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                  |
| regex_dna                | 221 ms                                                     | 228 ms: 1.03x slower                                                  |
| python_startup           | 10.8 ms                                                    | 11.1 ms: 1.03x slower                                                 |
| generators               | 29.6 ms                                                    | 30.7 ms: 1.03x slower                                                 |
| pycparser                | 1.16 sec                                                   | 1.20 sec: 1.04x slower                                                |
| regex_effbot             | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 635 ms: 1.04x slower                                                  |
| go                       | 145 ms                                                     | 151 ms: 1.04x slower                                                  |
| docutils                 | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                |
| django_template          | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| typing_runtime_protocols | 165 us                                                     | 172 us: 1.04x slower                                                  |
| pickle_dict              | 34.8 us                                                    | 36.4 us: 1.05x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.60 ms: 1.05x slower                                                 |
| genshi_text              | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                                 |
| raytrace                 | 267 ms                                                     | 281 ms: 1.05x slower                                                  |
| bench_thread_pool        | 834 us                                                     | 878 us: 1.05x slower                                                  |
| pickle                   | 11.5 us                                                    | 12.1 us: 1.05x slower                                                 |
| nqueens                  | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                                 |
| async_generators         | 442 ms                                                     | 467 ms: 1.06x slower                                                  |
| pickle_list              | 5.11 us                                                    | 5.40 us: 1.06x slower                                                 |
| sympy_str                | 282 ms                                                     | 302 ms: 1.07x slower                                                  |
| python_startup_no_site   | 7.11 ms                                                    | 7.59 ms: 1.07x slower                                                 |
| scimark_sor              | 127 ms                                                     | 137 ms: 1.08x slower                                                  |
| sympy_expand             | 473 ms                                                     | 514 ms: 1.09x slower                                                  |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| sympy_sum                | 156 ms                                                     | 172 ms: 1.10x slower                                                  |
| pylint                   | 317 ms                                                     | 352 ms: 1.11x slower                                                  |
| genshi_xml               | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                 |
| deltablue                | 3.25 ms                                                    | 3.75 ms: 1.15x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (13): deepcopy_memo, logging_simple, sqlglot_transpile, async_tree_none, asyncio_websockets, html5lib, async_tree_memoization_tg, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_none_tg, unpickle, async_tree_io, async_tree_memoization
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 73.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x