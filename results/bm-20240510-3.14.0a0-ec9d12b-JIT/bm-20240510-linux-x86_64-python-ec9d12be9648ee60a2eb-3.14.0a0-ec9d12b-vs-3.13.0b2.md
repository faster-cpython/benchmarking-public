# Results vs. 3.13.0b2

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.03x slower
- HPT reliability: 75.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 280 ms: 1.02x slower                                                  |
| chameleon      | 7.22 ms                                                    | 7.00 ms: 1.03x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                |
| html5lib       | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                 |
| tornado_http   | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 378 ms                                                     | 365 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed | 611 ms                                                     | 627 ms: 1.03x slower                                                  |
| async_tree_none_tg      | 336 ms                                                     | 349 ms: 1.04x slower                                                  |
| async_tree_io_tg        | 936 ms                                                     | 986 ms: 1.05x slower                                                  |
| Geometric mean          | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                 |
| nbody          | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                 |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.04x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                 |
| regex_dna      | 221 ms                                                     | 214 ms: 1.03x faster                                                  |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 152 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 33.5 us: 1.04x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 59.1 ms: 1.03x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 29.1 us: 1.01x slower                                                 |
| unpickle_pure_python | 218 us                                                     | 222 us: 1.02x slower                                                  |
| unpickle_list        | 5.34 us                                                    | 5.44 us: 1.02x slower                                                 |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| unpickle             | 15.1 us                                                    | 15.6 us: 1.03x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.47 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 11.0 ms: 1.02x slower                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.56 ms: 1.18x faster                                                 |
| genshi_text     | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                 |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|--------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_fft              | 392 ms                                                     | 319 ms: 1.23x faster                                                  |
| richards                 | 50.9 ms                                                    | 41.8 ms: 1.22x faster                                                 |
| richards_super           | 57.4 ms                                                    | 47.6 ms: 1.20x faster                                                 |
| mako                     | 11.2 ms                                                    | 9.56 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                 |
| crypto_pyaes             | 77.5 ms                                                    | 67.9 ms: 1.14x faster                                                 |
| spectral_norm            | 116 ms                                                     | 102 ms: 1.14x faster                                                  |
| float                    | 78.9 ms                                                    | 71.6 ms: 1.10x faster                                                 |
| nbody                    | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 63.4 ms: 1.09x faster                                                 |
| tomli_loads              | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                |
| fannkuch                 | 402 ms                                                     | 371 ms: 1.08x faster                                                  |
| pprint_pformat           | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                                |
| pprint_safe_repr         | 758 ms                                                     | 708 ms: 1.07x faster                                                  |
| xml_etree_parse          | 162 ms                                                     | 152 ms: 1.07x faster                                                  |
| xml_etree_iterparse      | 107 ms                                                     | 101 ms: 1.06x faster                                                  |
| pyflate                  | 484 ms                                                     | 459 ms: 1.05x faster                                                  |
| xml_etree_generate       | 87.4 ms                                                    | 83.1 ms: 1.05x faster                                                 |
| deepcopy_memo            | 39.7 us                                                    | 37.9 us: 1.05x faster                                                 |
| sqlite_synth             | 2.99 us                                                    | 2.87 us: 1.04x faster                                                 |
| pickle_dict              | 34.8 us                                                    | 33.5 us: 1.04x faster                                                 |
| regex_v8                 | 25.1 ms                                                    | 24.3 ms: 1.04x faster                                                 |
| async_tree_none          | 378 ms                                                     | 365 ms: 1.04x faster                                                  |
| regex_effbot             | 3.67 ms                                                    | 3.55 ms: 1.04x faster                                                 |
| xml_etree_process        | 61.2 ms                                                    | 59.1 ms: 1.03x faster                                                 |
| chaos                    | 61.3 ms                                                    | 59.3 ms: 1.03x faster                                                 |
| regex_dna                | 221 ms                                                     | 214 ms: 1.03x faster                                                  |
| json_dumps               | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| chameleon                | 7.22 ms                                                    | 7.00 ms: 1.03x faster                                                 |
| logging_format           | 6.47 us                                                    | 6.28 us: 1.03x faster                                                 |
| gc_traversal             | 3.98 ms                                                    | 3.87 ms: 1.03x faster                                                 |
| mdp                      | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                                |
| pickle_pure_python       | 305 us                                                     | 300 us: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                     | 188 ms: 1.02x faster                                                  |
| coroutines               | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                    | 1.64 ms: 1.00x slower                                                 |
| meteor_contest           | 110 ms                                                     | 110 ms: 1.01x slower                                                  |
| json_loads               | 28.9 us                                                    | 29.1 us: 1.01x slower                                                 |
| html5lib                 | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                 |
| create_gc_cycles         | 1.82 ms                                                    | 1.83 ms: 1.01x slower                                                 |
| thrift                   | 823 us                                                     | 830 us: 1.01x slower                                                  |
| logging_silent           | 105 ns                                                     | 106 ns: 1.01x slower                                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 1.86 sec: 1.01x slower                                                |
| json                     | 5.31 ms                                                    | 5.39 ms: 1.01x slower                                                 |
| unpickle_pure_python     | 218 us                                                     | 222 us: 1.02x slower                                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 56.5 ms: 1.02x slower                                                 |
| regex_compile            | 137 ms                                                     | 139 ms: 1.02x slower                                                  |
| unpickle_list            | 5.34 us                                                    | 5.44 us: 1.02x slower                                                 |
| python_startup           | 10.8 ms                                                    | 11.0 ms: 1.02x slower                                                 |
| 2to3                     | 274 ms                                                     | 280 ms: 1.02x slower                                                  |
| sqlglot_normalize        | 110 ms                                                     | 112 ms: 1.02x slower                                                  |
| coverage                 | 93.1 ms                                                    | 95.1 ms: 1.02x slower                                                 |
| generators               | 29.6 ms                                                    | 30.3 ms: 1.02x slower                                                 |
| pathlib                  | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                                 |
| dask                     | 369 ms                                                     | 379 ms: 1.02x slower                                                  |
| flaskblogging            | 9.01 ms                                                    | 9.23 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 627 ms: 1.03x slower                                                  |
| pickle                   | 11.5 us                                                    | 11.8 us: 1.03x slower                                                 |
| scimark_lu               | 122 ms                                                     | 125 ms: 1.03x slower                                                  |
| asyncio_tcp              | 508 ms                                                     | 522 ms: 1.03x slower                                                  |
| deepcopy                 | 367 us                                                     | 378 us: 1.03x slower                                                  |
| tornado_http             | 94.6 ms                                                    | 97.6 ms: 1.03x slower                                                 |
| unpickle                 | 15.1 us                                                    | 15.6 us: 1.03x slower                                                 |
| go                       | 145 ms                                                     | 149 ms: 1.03x slower                                                  |
| dulwich_log              | 67.2 ms                                                    | 69.6 ms: 1.04x slower                                                 |
| async_tree_none_tg       | 336 ms                                                     | 349 ms: 1.04x slower                                                  |
| typing_runtime_protocols | 165 us                                                     | 171 us: 1.04x slower                                                  |
| genshi_text              | 23.7 ms                                                    | 24.7 ms: 1.04x slower                                                 |
| raytrace                 | 267 ms                                                     | 278 ms: 1.04x slower                                                  |
| django_template          | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                 |
| hexiom                   | 6.30 ms                                                    | 6.58 ms: 1.05x slower                                                 |
| docutils                 | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                |
| bench_thread_pool        | 834 us                                                     | 877 us: 1.05x slower                                                  |
| async_tree_io_tg         | 936 ms                                                     | 986 ms: 1.05x slower                                                  |
| async_generators         | 442 ms                                                     | 466 ms: 1.05x slower                                                  |
| scimark_sor              | 127 ms                                                     | 136 ms: 1.06x slower                                                  |
| sympy_str                | 282 ms                                                     | 301 ms: 1.07x slower                                                  |
| nqueens                  | 81.4 ms                                                    | 87.0 ms: 1.07x slower                                                 |
| pickle_list              | 5.11 us                                                    | 5.47 us: 1.07x slower                                                 |
| python_startup_no_site   | 7.11 ms                                                    | 7.63 ms: 1.07x slower                                                 |
| sympy_expand             | 473 ms                                                     | 510 ms: 1.08x slower                                                  |
| sympy_integrate          | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                 |
| sympy_sum                | 156 ms                                                     | 172 ms: 1.10x slower                                                  |
| pylint                   | 317 ms                                                     | 354 ms: 1.12x slower                                                  |
| genshi_xml               | 51.6 ms                                                    | 57.9 ms: 1.12x slower                                                 |
| deltablue                | 3.25 ms                                                    | 3.73 ms: 1.15x slower                                                 |
| telco                    | 8.41 ms                                                    | 173 ms: 20.54x slower                                                 |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (10): pycparser, logging_simple, asyncio_websockets, deepcopy_reduce, async_tree_io, comprehensions, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 75.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x